import argparse
import cv2
import mmcv
import torch
import json
import os
from mmengine.dataset import Compose
from mmdet.apis import init_detector
from mmengine.utils import track_iter_progress
from mmyolo.registry import VISUALIZERS

def parse_args():
    parser = argparse.ArgumentParser(description='YOLO-World video demo')
    parser.add_argument('--config', help='test config file path',
                        default=r"C:\Users\Administrator\PycharmProjects\hello_world\YOLO-World\demo\yolo_world_v2_l_vlpan_bn_2e-3_100e_4x8gpus_obj365v1_goldg_train_1280ft_lvis_minival.py")
    parser.add_argument('--checkpoint', help='checkpoint file',
                        default="yolo_world_v2_l_obj365v1_goldg_pretrain_1280ft-9babe3f6.pth")
    parser.add_argument('--video_dir', help='video directory path', default="video_folder")
    parser.add_argument('--text', help='text prompts, including categories separated by a comma or a txt file with each line as a prompt.',
                        default=',,,,,,,,car')
    parser.add_argument('--device', default='cuda:0', help='device used for inference')
    parser.add_argument('--score-thr', default=0.1, type=float, help='confidence score threshold for predictions.')
    parser.add_argument('--out_dir', type=str, help='output directory for videos', default="output_videos")
    args = parser.parse_args()
    return args

def inference_detector(model, image, texts, test_pipeline, score_thr=0.3):
    data_info = dict(img_id=0, img=image, texts=texts)
    print("texts:", texts)  # 打印文本提示
    data_info = test_pipeline(data_info)
    data_batch = dict(inputs=data_info['inputs'].unsqueeze(0),
                      data_samples=[data_info['data_samples']])

    with torch.no_grad():
        output = model.test_step(data_batch)[0]
        pred_instances = output.pred_instances
        pred_instances = pred_instances[pred_instances.scores.float() > score_thr]
    output.pred_instances = pred_instances
    return output

def process_video(model, video_path, texts, test_pipeline, score_thr, out_dir):
    visualizer = VISUALIZERS.build(model.cfg.visualizer)
    visualizer.dataset_meta = model.dataset_meta

    video_reader = mmcv.VideoReader(video_path)
    video_writer = None
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_video_path = os.path.join(out_dir, os.path.basename(video_path))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(out_video_path, fourcc, video_reader.fps, (video_reader.width, video_reader.height))

    import sys
    frames = [frame for frame in video_reader]
    detected = False  # 初始化检测标志
    detected_object = None  # 初始化检测到的对象
    for frame in track_iter_progress(frames, file=sys.stdout):
        if detected:
            break  # 如果已经检测到目标对象，则跳出外部循环

        result = inference_detector(model, frame, texts, test_pipeline, score_thr=score_thr)

        # 打印推理结果的所有属性
        for instance in result.pred_instances:
            if hasattr(instance, 'labels'):
                label_index = instance.labels.item()
                print("Predicted label index:", label_index)
                # 打印实际类别名称
                label_name = model.dataset_meta['classes'][label_index]
                print("Predicted label name:", label_name)
                if label_name in [text[0].strip() for text in texts]:
                    print(f"Detected target object '{label_name}' in the video.")
                    detected = True  # 设置检测标志
                    detected_object = label_name  # 保存检测到的对象
                    break  # 检测到目标对象后跳出内部循环
            else:
                print("No label found for this instance")

    if detected and detected_object:
        # 创建JSONL文件并写入检测到的信息
        output_data = {
            "video_name": os.path.basename(video_path),
            "detected_object": detected_object
        }
        with open("detection_result.jsonl", "a") as json_file:
            json_file.write(json.dumps(output_data) + "\n")
        print("Detection result saved to detection_result.jsonl")

def main():
    args = parse_args()

    model = init_detector(args.config, args.checkpoint, device=args.device)

    # build test pipeline
    model.cfg.test_dataloader.dataset.pipeline[0].type = 'mmdet.LoadImageFromNDArray'
    test_pipeline = Compose(model.cfg.test_dataloader.dataset.pipeline)

    if args.text.endswith('.txt'):
        with open(args.text) as f:
            lines = f.readlines()
        texts = [[t.rstrip('\r\n')] for t in lines] + [[' ']]
    else:
        texts = [[t.strip()] for t in args.text.split(',')] + [[' ']]

    # 打印模型的类别标签
    print("Model categories:", model.dataset_meta['classes'])

    # reparameterize texts
    model.reparameterize(texts)

    video_files = [os.path.join(args.video_dir, f) for f in os.listdir(args.video_dir) if f.endswith(('.mp4', '.avi'))]
    for video_file in video_files:
        print(f"Processing video: {video_file}")
        process_video(model, video_file, texts, test_pipeline, args.score_thr, args.out_dir)

if __name__ == '__main__':
    main()
