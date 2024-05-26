import os
import traceback
from typing import Dict, Union

import cv2
import mmcv
import numpy as np
import torch
import pathlib as plb
from models.i3d.i3d_src.i3d_net import I3D
from models.i3d.transforms.transforms import (Clamp, PermuteAndUnsqueeze,
                                              PILToTensor, ResizeImproved,
                                              ScaleTo1_1, TensorCenterCrop,
                                              ToFloat, ToUInt8)
from models.raft.raft_src.raft import InputPadder
from torchvision import transforms
from tqdm import tqdm

from utils.utils import (action_on_extraction, form_list_from_user_input,
                         reencode_video_with_diff_fps,
                         show_predictions_on_dataset)

PWC_MODEL_PATH = './models/pwc/checkpoints/pwc_net_sintel.pt'
RAFT_MODEL_PATH = './models/raft/checkpoints/raft-sintel.pth'
I3D_RGB_PATH = './models/i3d/checkpoints/i3d_rgb.pt'
I3D_FLOW_PATH = './models/i3d/checkpoints/i3d_flow.pt'
PRE_CENTRAL_CROP_MIN_SIDE_SIZE = 256
CENTRAL_CROP_MIN_SIDE_SIZE = 224
DEFAULT_I3D_STEP_SIZE = 64
DEFAULT_I3D_STACK_SIZE = 64
I3D_CLASSES_NUM = 400

class ExtractI3D(torch.nn.Module):

    def __init__(self, args, external_call=False):
        super(ExtractI3D, self).__init__()
        self.feature_type = args.feature_type
        if args.streams is None:
            self.streams = ['rgb', 'flow']
        else:
            self.streams = args.streams
        self.path_list = form_list_from_user_input(args)
        self.flow_type = args.flow_type
        self.flow_model_paths = {'pwc': PWC_MODEL_PATH, 'raft': RAFT_MODEL_PATH}
        self.i3d_weights_paths = {'rgb': I3D_RGB_PATH, 'flow': I3D_FLOW_PATH}
        self.min_side_size = PRE_CENTRAL_CROP_MIN_SIDE_SIZE
        self.central_crop_size = CENTRAL_CROP_MIN_SIDE_SIZE
        self.extraction_fps = args.extraction_fps
        self.step_size = args.step_size
        self.stack_size = args.stack_size
        if self.step_size is None:
            self.step_size = DEFAULT_I3D_STEP_SIZE
        if self.stack_size is None:
            self.stack_size = DEFAULT_I3D_STACK_SIZE
        self.resize_transforms = transforms.Compose([
            transforms.ToPILImage(),
            ResizeImproved(self.min_side_size),
            PILToTensor(),
            ToFloat(),
        ])
        self.i3d_transforms = {
            'rgb': transforms.Compose([
                TensorCenterCrop(self.central_crop_size),
                ScaleTo1_1(),
                PermuteAndUnsqueeze()
            ]),
            'flow': transforms.Compose([
                TensorCenterCrop(self.central_crop_size),
                Clamp(-20, 20),
                ToUInt8(),
                ScaleTo1_1(),
                PermuteAndUnsqueeze()
            ])
        }
        self.show_pred = args.show_pred
        self.i3d_classes_num = I3D_CLASSES_NUM
        self.keep_tmp_files = args.keep_tmp_files
        self.on_extraction = args.on_extraction
        self.tmp_path = os.path.join(args.tmp_path, self.feature_type)
        # self.output_path = os.path.join(args.output_path, self.feature_type)
        self.external_call = external_call
        if external_call is False:
            self.output_direct = args.output_direct
            if self.output_direct is True:
                self.output_path = args.output_path
            else:
                self.output_path = os.path.join(args.output_path, self.feature_type)
        self.progress = tqdm(total=len(self.path_list))

    def forward(self, indices: torch.LongTensor):
        """
        Arguments:
            indices {torch.LongTensor} -- indices to self.path_list
        """
        device = indices.device

        if self.flow_type == 'pwc':
            from models.pwc.pwc_src.pwc_net import PWCNet
            flow_xtr_model = PWCNet()
            flow_xtr_model.load_state_dict(torch.load(self.flow_model_paths[self.flow_type], map_location=device))
            flow_xtr_model = flow_xtr_model.to(device)
            flow_xtr_model.eval()
        elif self.flow_type == 'raft':
            from models.raft.raft_src.raft import RAFT
            flow_xtr_model = RAFT()
            flow_xtr_model = torch.nn.DataParallel(flow_xtr_model, device_ids=[device])
            flow_xtr_model.load_state_dict(torch.load(self.flow_model_paths[self.flow_type], map_location=device))
            flow_xtr_model = flow_xtr_model.to(device)
            flow_xtr_model.eval()
        elif self.flow_type == 'flow':
            flow_xtr_model = None
        else:
            raise NotImplementedError

        models = {}
        for stream in self.streams:
            models[stream] = I3D(num_classes=self.i3d_classes_num, modality=stream).to(device).eval()
            models[stream].load_state_dict(torch.load(self.i3d_weights_paths[stream]))

        feats_list = []
        for idx in indices:
            # when error occurs might fail silently when run from torch data parallel
            try:
                # If `flow_dir` is on, the element of path_list will be like [path of video, dir of flow imgs]
                feats_dict = self.extract(device, flow_xtr_model, models, self.path_list[idx])
                if self.external_call is False:
                    action_on_extraction(feats_dict, self.path_list[idx], self.output_path, self.on_extraction)
                else:
                    feats_list.append(feats_dict)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except Exception as e:
                # traceback.print_exc()  # for the whole traceback
                print(e)
                print(f'Extraction failed at: {self.path_list[idx]}. Continuing extraction')

            # update tqdm progress bar
            self.progress.update()
        return feats_list

    def extract(self, device: torch.device, flow_xtr_model: torch.nn.Module,
                models: Dict[str, torch.nn.Module], video_path: Union[str, None] = None
                ) -> Dict[str, Union[torch.nn.Module, str]]:
        """The extraction call. Made to clean the forward call a bit.

        Arguments:
            device {torch.device}
            flow_xtr_model {torch.nn.Module}
            models {Dict[str, torch.nn.Module]}

        Keyword Arguments:
            video_path {Union[str, None]} -- if you would like to use import it and use it as
                                             "path -> model"-fashion (default: {None})
                                             If `flow_dir` is on, the element of path_list will
                                             be like [path of video, dir of flow images]

        Returns:
            Dict[str, Union[torch.nn.Module, str]] -- dict with i3d features and their type
        """
        def _run_on_a_stack(feats_dict, rgb_stack, models, device, stack_counter, padder=None):
            rgb_stack = torch.cat(rgb_stack).to(device)

            for stream in self.streams:
                with torch.no_grad():
                    # if i3d stream is flow, we first need to calculate optical flow, otherwise, we use rgb
                    # `end_idx-1` and `start_idx+1` because flow is calculated between f and f+1 frames
                    # we also use `end_idx-1` for stream == 'rgb' case: just to make sure the feature length
                    # is same regardless of whether only rgb is used or flow
                    if stream == 'flow':
                        if self.flow_type == 'raft':
                            # print(rgb_stack.shape, end="\t")
                            stream_slice = flow_xtr_model(padder.pad(rgb_stack)[:-1], padder.pad(rgb_stack)[1:])
                            # print(stream_slice.shape)  # torch.Size([64, 2, H, W])
                        elif self.flow_type == 'pwc':
                            stream_slice = flow_xtr_model(rgb_stack[:-1], rgb_stack[1:])
                        else:
                            raise NotImplementedError
                    elif stream == 'rgb':
                        stream_slice = rgb_stack[:-1]
                    else:
                        raise NotImplementedError

                    # apply transforms depending on the stream (flow or rgb)
                    stream_slice = self.i3d_transforms[stream](stream_slice)
                    # extract features for a stream
                    feats = models[stream](stream_slice, features=True)  # (B, 1024)
                    # add features to the output dict
                    feats_dict[stream].extend(feats.tolist())
                    # show predictions on a daataset
                    if self.show_pred:
                        softmaxes, logits = models[stream](stream_slice, features=False)  # (B, classes=400)
                        print(f'{video_path} @ stack {stack_counter} ({stream} stream)')
                        show_predictions_on_dataset(logits, 'kinetics')

        def _run_on_a_stack_flow(feats_dict, rgb_stack, flow_stack, models, device):
            rgb_stack = torch.cat(rgb_stack).to(device)

            for stream in self.streams:
                with torch.no_grad():
                    # if i3d stream is flow, we first need to calculate optical flow, otherwise, we use rgb
                    # `end_idx-1` and `start_idx+1` because flow is calculated between f and f+1 frames
                    # we also use `end_idx-1` for stream == 'rgb' case: just to make sure the feature length
                    # is same regardless of whether only rgb is used or flow
                    if stream == 'flow':
                        flow_stack_ts = []
                        for fl_x, fl_y in flow_stack:
                            # torch.Size([2, 256, 344])
                            flow_stack_ts.append(torch.stack([
                                torch.tensor(mmcv.imread(fl_x, flag='grayscale')),
                                torch.tensor(mmcv.imread(fl_y, flag='grayscale'))
                            ], dim=0))
                        # torch.Size([64, 2, 256, 344])
                        stream_slice = torch.stack(flow_stack_ts, dim=0).to(device)
                    elif stream == 'rgb':
                        stream_slice = rgb_stack[:-1]
                    else:
                        raise NotImplementedError

                    # apply transforms depending on the stream (flow or rgb)
                    stream_slice = self.i3d_transforms[stream](stream_slice)
                    # extract features for a stream
                    feats = models[stream](stream_slice, features=True)  # (B, 1024)
                    # add features to the output dict
                    feats_dict[stream].extend(feats.tolist())
                    # show predictions on a daataset
                    if self.show_pred and stream == 'flow':
                        softmaxes, logits = models[stream](stream_slice, features=False)  # (B, classes=400)
                        print(f'{video_path} @ stack {stack_counter} ({stream} stream)')
                        show_predictions_on_dataset(logits, 'kinetics')

        if self.flow_type == 'flow':
            video = mmcv.VideoReader(video_path[0])
            flow_x = list(plb.Path(video_path[1]).glob("flow_x*.jpg"))
            flow_x.sort(key=lambda x: x.stem[7:])
            flow_y = list(plb.Path(video_path[1]).glob("flow_y*.jpg"))
            flow_y.sort(key=lambda x: x.stem[7:])
            flows = list(zip(flow_x, flow_y))
        else:
            video = mmcv.VideoReader(video_path)
        fps, frame_cnt = video.fps, video.frame_cnt
        mspf = 0.001 / fps  # ms per frame

        # Load rgb frames from video
        if self.extraction_fps is not None:  # when fps is a fix number
            samples_num = int(frame_cnt / fps * self.extraction_fps)  # get num of sample frame to be extracted
            samples_ix = np.linspace(1, frame_cnt - 1, samples_num).astype(int)
            frames = [video.get_frame(i) for i in samples_ix]
            frames = [i for i in frames if i is not None]  # make sure no NoneType in frames
            timestamps_ms = [i * mspf for i in samples_ix]
        elif frame_cnt < DEFAULT_I3D_STACK_SIZE + 1:  # not enough frames
            samples_num = DEFAULT_I3D_STACK_SIZE + 1
            samples_ix = np.linspace(1, frame_cnt - 1, samples_num).astype(int)
            frames = [video.get_frame(i) for i in samples_ix]
            frames = [i for i in frames if i is not None]  # make sure no NoneType in frames
            timestamps_ms = [i * mspf for i in samples_ix]
        else:  # get all frames
            frames = [video.get_frame(i) for i in range(frame_cnt)]
            frames = [i for i in frames if i is not None]  # make sure no NoneType in frames
            timestamps_ms = [i * mspf for i in range(frame_cnt)]

        # Gradually feed rgb frame into stack
        # If length of stack meet DEFAULT_I3D_STACK_SIZE then do a extraction
        # and go forward DEFAULT_I3D_STEP_SIZE.
        feats_dict = {stream: [] for stream in self.streams}  # {rgb: [], flow: []}
        stack_counter = 0
        if self.flow_type == 'flow':
            rgb_stack, flow_stack = [], []
            for rgb, flow in zip(frames, flows):
                rgb = self.resize_transforms(rgb)
                rgb = rgb.unsqueeze(0)
                rgb_stack.append(rgb)
                flow_stack.append(flow)

                if len(rgb_stack) == self.stack_size:
                    _run_on_a_stack_flow(feats_dict, rgb_stack, flow_stack, models, device)
                    rgb_stack = rgb_stack[self.step_size:]
                    flow_stack = flow_stack[self.step_size:]
                    stack_counter += 1
        else:
            rgb_stack = []
            padder = None
            # print(f"Length of frames: {len(frames)}")
            for rgb in frames:
                rgb = self.resize_transforms(rgb)
                rgb = rgb.unsqueeze(0)
                rgb_stack.append(rgb)

                if self.flow_type == 'raft' and padder is None:
                    padder = InputPadder(rgb.shape)
                # - 1 is used because we need B+1 frames to calculate B frames
                if len(rgb_stack) - 1 == self.stack_size:
                    _run_on_a_stack(feats_dict, rgb_stack, models, device, stack_counter, padder)
                    # leaving the elements if step_size < stack_size so they will not be loaded again
                    # if step_size == stack_size one element is left because the flow between the last element
                    # in the prev list and the first element in the current list
                    rgb_stack = rgb_stack[self.step_size:]
                    stack_counter += 1

        feats_dict = {stream: np.array(feats) for stream, feats in feats_dict.items()}
        # also include the timestamps and fps
        feats_dict['fps'] = np.array(fps)
        feats_dict['timestamps_ms'] = np.array(timestamps_ms)

        return feats_dict
