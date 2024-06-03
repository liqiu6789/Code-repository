import argparse
import torch
from llavavid.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llavavid.conversation import conv_templates, SeparatorStyle
from llavavid.model.builder import load_pretrained_model
from llavavid.utils import disable_torch_init
from llavavid.mm_utils import tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria
import json
import os
import math
from tqdm import tqdm
from decord import VideoReader, cpu
from transformers import AutoConfig
import time
import numpy as np
import multiprocessing

def split_list(lst, n):
    """Split a list into n (roughly) equal-sized chunks"""
    chunk_size = math.ceil(len(lst) / n)  # integer division
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]

def get_chunk(lst, n, k):
    chunks = split_list(lst, n)
    return chunks[k]

def parse_args():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_dir", help="Directory containing the video files.", required=True)
    parser.add_argument("--output_dir", help="Directory to save the model results JSON.", required=True)
    parser.add_argument("--output_name", help="Base name of the file for storing results JSON.", required=True)
    parser.add_argument("--model-path", type=str, default="facebook/opt-350m")
    parser.add_argument("--model-base", type=str, default=None)
    parser.add_argument("--conv-mode", type=str, default=None)
    parser.add_argument("--mm_resampler_type", type=str, default="spatial_pool")
    parser.add_argument("--mm_spatial_pool_stride", type=int, default=4)
    parser.add_argument("--mm_spatial_pool_out_channels", type=int, default=1024)
    parser.add_argument("--mm_spatial_pool_mode", type=str, default="average")
    parser.add_argument("--image_aspect_ratio", type=str, default="anyres")
    parser.add_argument("--image_grid_pinpoints", type=str, default="[(224, 448), (224, 672), (224, 896), (448, 448), (448, 224), (672, 224), (896, 224)]")
    parser.add_argument("--mm_patch_merge_type", type=str, default="spatial_unpad")
    parser.add_argument("--overwrite", type=lambda x: (str(x).lower() == 'true'), default=True)
    parser.add_argument("--for_get_frames_num", type=int, default=4)
    parser.add_argument("--load_8bit",  type=lambda x: (str(x).lower() == 'true'), default=False)
    return parser.parse_args()

def load_video(video_path, args):
    vr = VideoReader(video_path, ctx=cpu(0))
    total_frame_num = len(vr)
    uniform_sampled_frames = np.linspace(0, total_frame_num - 1, args.for_get_frames_num, dtype=int)
    frame_idx = uniform_sampled_frames.tolist()
    spare_frames = vr.get_batch(frame_idx).asnumpy()
    return spare_frames

def run_inference_for_video(args, video_path, gpu_id):
    torch.cuda.set_device(gpu_id)
    model_name = get_model_name_from_path(args.model_path)
    if args.overwrite:
        overwrite_config = {
            "mm_resampler_type": args.mm_resampler_type,
            "mm_spatial_pool_stride": args.mm_spatial_pool_stride,
            "mm_spatial_pool_out_channels": args.mm_spatial_pool_out_channels,
            "mm_spatial_pool_mode": args.mm_spatial_pool_mode,
            "patchify_video_feature": False
        }
        cfg_pretrained = AutoConfig.from_pretrained(args.model_path)
        if "224" in cfg_pretrained.mm_vision_tower:
            least_token_number = args.for_get_frames_num * (16 // args.mm_spatial_pool_stride) ** 2 + 1000
        else:
            least_token_number = args.for_get_frames_num * (24 // args.mm_spatial_pool_stride) ** 2 + 1000
        scaling_factor = math.ceil(least_token_number / 4096)
        if scaling_factor >= 2 and "mistral" not in cfg_pretrained._name_or_path.lower() and "7b" in cfg_pretrained._name_or_path.lower():
            overwrite_config["rope_scaling"] = {"factor": float(scaling_factor), "type": "linear"}
        overwrite_config["max_sequence_length"] = 4096 * scaling_factor
        overwrite_config["tokenizer_model_max_length"] = 4096 * scaling_factor
        tokenizer, model, image_processor, context_len = load_pretrained_model(args.model_path, args.model_base, model_name, load_8bit=args.load_8bit, overwrite_config=overwrite_config)
    else:
        tokenizer, model, image_processor, context_len = load_pretrained_model(args.model_path, args.model_base, model_name)

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    output_name = os.path.splitext(os.path.basename(video_path))[0]
    answers_file = os.path.join(args.output_dir, f"{output_name}.json")

    sample_set = {"Q": "Please provide a detailed description of the video, focusing on the main subjects, their actions, and the background scenes", "video_name": video_path}

    if os.path.exists(video_path):
        video = load_video(video_path, args)
        video = image_processor.preprocess(video, return_tensors="pt")["pixel_values"].half().cuda()
        video = [video]

    question = sample_set["Q"]
    if model.config.mm_use_im_start_end:
        question = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + "\n" + question
    else:
        question = DEFAULT_IMAGE_TOKEN + "\n" + question

    conv = conv_templates[args.conv_mode].copy()
    conv.append_message(conv.roles[0], question)
    conv.append_message(conv.roles[1], None)
    prompt = conv.get_prompt()

    input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors="pt").unsqueeze(0).cuda()
    attention_masks = input_ids.ne(tokenizer.pad_token_id).long().cuda()

    stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
    keywords = [stop_str]
    stopping_criteria = KeywordsStoppingCriteria(keywords, tokenizer, input_ids)

    cur_prompt = sample_set["Q"]
    with torch.inference_mode():
        model.update_prompt([[cur_prompt]])
        start_time = time.time()
        output_ids = model.generate(inputs=input_ids, images=video, attention_mask=attention_masks, modalities="video", do_sample=True, temperature=0.2, max_new_tokens=1024, use_cache=True, stopping_criteria=[stopping_criteria])
        end_time = time.time()
        print(f"Time taken for inference on GPU {gpu_id}: {end_time - start_time} seconds")

    outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()
    if outputs.endswith(stop_str):
        outputs = outputs[: -len(stop_str)]
    outputs = outputs.strip()

    sample_set["pred"] = outputs
    with open(answers_file, "w") as ans_file:
        json.dump(sample_set, ans_file, indent=4)

def run_inference(args):
    video_files = [os.path.join(args.video_dir, f) for f in os.listdir(args.video_dir) if f.endswith('.mp4')]
    num_gpus = torch.cuda.device_count()
    tasks = [(args, video, gpu_id % num_gpus) for gpu_id, video in enumerate(video_files)]

    with multiprocessing.Pool(num_gpus) as pool:
        pool.starmap(run_inference_for_video, tasks)

if __name__ == "__main__":
    args = parse_args()
    run_inference(args)
