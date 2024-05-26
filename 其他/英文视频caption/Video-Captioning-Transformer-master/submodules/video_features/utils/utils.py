import argparse
import os
import sys
import pathlib as plb
import subprocess
from typing import Dict, List
import pickle
from PIL import Image

import numpy as np
import torch
import torch.nn.functional as F
import mmcv

IMAGENET_CLASS_PATH = './utils/IN_label_map.txt'
KINETICS_CLASS_PATH = './utils/K400_label_map.txt'


def show_predictions_on_dataset(logits: torch.FloatTensor, dataset: str):
    """Prints out predictions for each feature

    Args:
        logits (torch.FloatTensor): after-classification layer vector (B, classes)
        dataset (str): which dataset to use to show the predictions on. In ('imagenet', 'kinetics')
    """
    if dataset == 'kinetics':
        path_to_class_list = KINETICS_CLASS_PATH
    elif dataset == 'imagenet':
        path_to_class_list = IMAGENET_CLASS_PATH
    else:
        raise NotImplementedError

    dataset_classes = [x.strip() for x in open(path_to_class_list)]

    # Show predictions
    softmaxes = F.softmax(logits, dim=-1)
    top_val, top_idx = torch.sort(softmaxes, dim=-1, descending=True)

    k = 5
    logits_score = logits.gather(1, top_idx[:, :k]).tolist()
    softmax_score = softmaxes.gather(1, top_idx[:, :k]).tolist()
    class_labels = [[dataset_classes[idx] for idx in i_row] for i_row in top_idx[:, :k]]

    for b in range(len(logits)):
        for (logit, smax, cls) in zip(logits_score[b], softmax_score[b], class_labels[b]):
            print(f'{logit:.3f} {smax:.3f} {cls}')
        print()


def action_on_extraction(feats_dict: Dict[str, np.ndarray], video_path, output_path,
                         on_extraction: str, output_direct: bool = False):
    """What is going to be done with the extracted features.

    Args:
        output_direct (bool): whether or not to add feature type in output file name
        feats_dict (Dict[str, np.ndarray]): A dict with features and possibly some meta. Key will be used as
                                            suffixes to the saved files if `save_numpy` or `save_pickle` is
                                            used.
                                            {self.feature_type, 'fps', 'timestamps_ms'}
        video_path (str or List(str)): A path to the video or a list where the video path is the first element.
        on_extraction (str): What to do with the features on extraction.
        output_path (str): Where to save the features if `save_numpy` or `save_pickle` is used.
    """
    suffix = {'save_numpy': 'npy', 'save_pickle': 'pkl'}
    if type(video_path) is list or type(video_path) is tuple:  # avoid certain mistakes
        video_path = video_path[0]
    name = plb.Path(video_path).stem
    # since the features are enclosed in a dict with another meta information we will iterate on kv
    for key, value in feats_dict.items():
        # don't save fps and timestamp
        if key in ['fps', 'timestamps_ms']:
            continue
        # print/save_numpy/save_pickle/save_jpg
        if on_extraction == 'print':
            print(key)
            print(value)
            print(f'max: {value.max():.8f}; mean: {value.mean():.8f}; min: {value.min():.8f}')
            print()
        elif on_extraction in ['save_numpy', 'save_pickle']:
            # make dir if doesn't exist
            os.makedirs(output_path, exist_ok=True)
            # extract file name and change the extension
            if output_direct is True:
                fname = f'{name}.{suffix[on_extraction]}'
            else:
                fname = f'{name}_{key}.{suffix[on_extraction]}'
            fpath = os.path.join(output_path, fname)
            # warning if err may happen
            if len(value) == 0:
                print(f'Warning: the value is empty for {key} @ {fpath}')
            # save
            if on_extraction == 'save_numpy':
                np.save(fpath, value)
            else:
                pickle.dump(value, open(fpath, 'wb'))
        elif on_extraction == 'save_jpg' and key in ['raft']:
            # make dir if doesn't exist
            os.makedirs(output_path, exist_ok=True)
            # warning if err may happen
            if len(value) == 0:
                print(f'Warning: the value is empty for {key} @ {name}')
            # make a directory to save pics
            path = os.path.join(output_path, name)
            os.makedirs(path)
            for f_num in value.shape[0]:
                # construct the paths to save the features
                img_x, img_y = Image.fromarray(value[f_num, 0]), Image.fromarray(value[f_num, 1])
                fpath_x = os.path.join(path, '{:0>5d}_x.jpg'.format(f_num))
                fpath_y = os.path.join(path, '{:0>5d}_y.jpg'.format(f_num))
                # save the info behind the each key
                img_x.convert('L').save(fpath_x)
                img_y.convert('L').save(fpath_y)
        else:
            raise NotImplementedError(f'on_extraction: {on_extraction} is not implemented')


def form_slices(size: int, stack_size: int, step_size: int):
    """print(form_slices(100, 15, 15) - example"""
    slices = []
    # calc how many full stacks can be formed out of framepaths
    full_stack_num = (size - stack_size) // step_size + 1
    for i in range(full_stack_num):
        start_idx = i * step_size
        end_idx = start_idx + stack_size
        slices.append((start_idx, end_idx))
    return slices


def sanity_check(args: argparse.Namespace):
    """Checks the prased user arguments.

    Args:
        args (argparse.Namespace): Parsed user arguments
    """
    assert os.path.relpath(args.output_path) != os.path.relpath(args.tmp_path), 'The same path for out & tmp'
    if args.show_pred:
        print('You want to see predictions. So, I will use only the first GPU from the list you specified.')
        args.device_ids = [args.device_ids[0]]
        if args.feature_type == 'vggish':
            print('Showing class predictions is not implemented for VGGish')
    if args.feature_type == 'r21d_rgb':
        message = 'torchvision.read_video only supports extraction at orig fps. Remove this argument.'
        assert args.extraction_fps is None, message
    if args.feature_type == 'i3d':
        message = f'I3D model does not support inputs shorter than 10 timestamps. You have: {args.stack_size}'
        if args.stack_size is not None:
            assert args.stack_size >= 10, message
    if args.feature_type in ['resnet18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'r21d_rgb']:
        if args.keep_tmp_files:
            print('If you want to keep frames while extracting features, please create an issue')


def form_list_from_user_input(args: argparse.Namespace) -> list:
    """User specifies either list of videos in the cmd or a path to a file with video paths. This function
    transforms the user input into a list of paths.
    If use existing flow images, args.flow_dir or args.flow_paths should be provided. Therefore each path
    of path_list has two elements.

    Args:
        args (argparse.Namespace): Parsed user arguments

    Returns:
        list: list with paths
    """
    if args.file_with_video_paths is not None:
        with open(args.file_with_video_paths) as rfile:
            # remove carriage return
            path_list = [line.replace('\n', '') for line in rfile.readlines()]
            # remove empty lines
            path_list = [path for path in path_list if len(path) > 0]
    elif args.video_dir is not None:
        if args.flow_dir is None:
            path_list = [str(i) for i in plb.Path(args.video_dir).glob("*")]
        else:
            path_list = []
            v_list, f_list = list(plb.Path(args.video_dir).glob("*")), list(plb.Path(args.flow_dir).glob("*"))
            v_list.sort(key=lambda x: x.stem)
            f_list.sort(key=lambda x: x.stem)
            for path_video, path_flow in zip(v_list, f_list):
                if path_video.stem == path_flow.stem:
                    path_list.append((str(path_video), str(path_flow)))
    elif args.video_paths is not None:
        if args.flow_paths is None:
            path_list = args.video_paths
        else:
            path_list = []
            for path_video, path_flow in zip(args.video_paths, args.flow_paths):
                if plb.Path(path_video).stem == plb.Path(path_flow).stem:
                    path_list.append((path_video, path_flow))
    else:
        raise ValueError('no video provided')

    # sanity check: prints paths which do not exist
    for path in path_list:
        if type(path) is tuple:
            assert os.path.exists(path[0])
            assert os.path.exists(path[1])
        else:
            not_exist = not os.path.exists(path)
            if not_exist:
                print(f'The path does not exist: {path}')
                raise ValueError('path not exist')

    return path_list


def which_ffmpeg() -> str:
    """Determines the path to ffmpeg library

    Returns:
        str -- path to the library
    """
    if 'linux' in sys.platform:
        result = subprocess.run(['which', 'ffmpeg'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ffmpeg_path = result.stdout.decode('utf-8').replace('\n', '')
    else:
        # result = subprocess.run(['Get-Command', 'ffmpeg'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        ffmpeg_path = "ffmpeg"
    return ffmpeg_path


def reencode_video_with_diff_fps(video_path: str, tmp_path: str, extraction_fps: float) -> str:
    """Reencodes the video given the path and saves it to the tmp_path folder.

    Args:
        video_path (str): original video
        tmp_path (str): the folder where tmp files are stored (will be appended with a proper filename).
        extraction_fps (float): target fps value

    Returns:
        str: The path where the tmp file is stored. To be used to load the video from
    """
    assert which_ffmpeg() != '', 'Is ffmpeg installed? Check if the conda environment is activated.'
    assert video_path.endswith('.mp4'), 'The file does not end with .mp4. Comment this if expected'
    # create tmp dir if doesn't exist
    os.makedirs(tmp_path, exist_ok=True)

    # form the path to tmp directory
    new_path = os.path.join(tmp_path, f'{plb.Path(video_path).stem}_new_fps.mp4')
    cmd = f'{which_ffmpeg()} -hide_banner -loglevel panic '
    cmd += f'-y -i {video_path} -filter:v fps=fps={extraction_fps} {new_path}'
    subprocess.call(cmd.split())

    return new_path


def extract_wav_from_mp4(video_path: str, tmp_path: str) -> str:
    """Extracts .wav file from .aac which is extracted from .mp4
    We cannot convert .mp4 to .wav directly. For this we do it in two stages: .mp4 -> .aac -> .wav

    Args:
        video_path (str): Path to a video
        audio_path_wo_ext (str):

    Returns:
        [str, str] -- path to the .wav and .aac audio
    """
    assert which_ffmpeg() != '', 'Is ffmpeg installed? Check if the conda environment is activated.'
    assert video_path.endswith('.mp4'), 'The file does not end with .mp4. Comment this if expected'
    # create tmp dir if doesn't exist
    os.makedirs(tmp_path, exist_ok=True)

    # extract video filename from the video_path
    video_filename = os.path.split(video_path)[-1].replace('.mp4', '')

    # the temp files will be saved in `tmp_path` with the same name
    audio_aac_path = os.path.join(tmp_path, f'{video_filename}.aac')
    audio_wav_path = os.path.join(tmp_path, f'{video_filename}.wav')

    # constructing shell commands and calling them
    mp4_to_acc = f'{which_ffmpeg()} -hide_banner -loglevel panic -y -i {video_path} -acodec copy {audio_aac_path}'
    aac_to_wav = f'{which_ffmpeg()} -hide_banner -loglevel panic -y -i {audio_aac_path} {audio_wav_path}'
    subprocess.call(mp4_to_acc.split())
    subprocess.call(aac_to_wav.split())

    return audio_wav_path, audio_aac_path


def fix_tensorflow_gpu_allocation(argparse_args):
    """tf somehow makes it impossible to specify a GPU index in the code, hence we use the env variable.
    To address this, we will assign the user-defined cuda ids to environment variable CUDA_VISIBLE_DEVICES.

    For example: if user specifies --device_ids 1 3 5 we will assign 1,3,5 to CUDA_VISIBLE_DEVICES environment
                 variable and reassign args.device_ids with [0, 1, 2] which are indices to the list of
                 user specified ids [1, 3, 5].

    Args:
        argparse_args (args): user-defined arguments from argparse
    """
    # argparse_args.device_ids are ints which cannot be joined with ','.join()
    device_ids = [str(index) for index in argparse_args.device_ids]
    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(device_ids)
    # [1, 3, 5] -> [0, 1, 2]
    argparse_args.device_ids = list(range(len(argparse_args.device_ids)))


def extract_frames(path: str, method: str):
    """
    Args:
        path: The video path that can be loaded directly
        method: <extract_method>_<parameters>
                e.g. fix_2    ->    fix fps of 2
                     uni_12   ->    uniformly samples 12 frames
    Returns:
        sample_idx, fps, timestamps_ms
    """
    print("&&&&&&&&&&&&&&",method)
    ext = method.split('_')[0]
    params = method.split('_')[1:]

    video = mmcv.VideoReader(str(path))  # H W C
    fps, frame_cnt = video.fps, video.frame_cnt
    mspf = 0.001 / fps  # ms per frame
    if ext == "fix":
        # get num of sample frame to be extracted
        samples_num = int(frame_cnt / fps * int(params[0]))
        # ignore some frames to avoid strange bugs
        samples_ix = np.linspace(1, frame_cnt - 2, samples_num).astype(int)
        timestamps_ms = [i * mspf for i in samples_ix]
        frames = []
        for idx in samples_ix:
            frames.append(video.get_frame(idx))
        return frames, fps, timestamps_ms
    elif ext == 'uni':
        samples_num = int(params[0])
        # ignore some frames to avoid strange bugs
        samples_ix = np.linspace(1, frame_cnt - 2, samples_num).astype(int)
        timestamps_ms = [i * mspf for i in samples_ix]
        frames = []
        for idx in samples_ix:
            frames.append(video.get_frame(idx))
        return frames, fps, timestamps_ms
    else:
        raise NotImplementedError(f'{ext} are not supported')
