import os
import pathlib
from typing import Dict, Union, Callable

import numpy as np
import torch
import clip
import mmcv
import PIL
from PIL import Image
from tqdm import tqdm
import traceback

if "submodules" in __name__:
    from ...utils.utils import (action_on_extraction, form_list_from_user_input, extract_frames)
else:
    from utils.utils import (action_on_extraction, form_list_from_user_input, extract_frames)


class ExtractCLIP(torch.nn.Module):

    def __init__(self, args, external_call=False):
        super(ExtractCLIP, self).__init__()
        self.feature_type = args.feature_type
        self.path_list = form_list_from_user_input(args)
        self.extraction_fps = args.extraction_fps
        self.extract_method = args.extract_method
        self.on_extraction = args.on_extraction
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

        # ['RN50', 'RN101', 'RN50x4', 'RN50x16', 'ViT-B/32', 'ViT-B/16']
        if self.feature_type == 'CLIP-ViT-B/32':
            model, preprocess = clip.load("ViT-B/32", device=device)
        elif self.feature_type == 'CLIP-ViT-B/16':
            model, preprocess = clip.load("ViT-B/16", device=device)
        elif self.feature_type == 'CLIP-RN50x16':
            model, preprocess = clip.load("RN50x16", device=device)
        elif self.feature_type == 'CLIP-RN50x4':
            model, preprocess = clip.load("RN50x4", device=device)
        elif self.feature_type == 'CLIP-RN101':
            model, preprocess = clip.load("RN101", device=device)
        elif self.feature_type == 'CLIP-RN50':
            model, preprocess = clip.load("RN50", device=device)
        elif self.feature_type == 'CLIP4CLIP-ViT-B-32':
            #model_path = os.path.join(pathlib.Path(__file__).parent, 'checkpoints', 'ViT-B/32"')
            # print("*********",model_path)
            # # print(model_path)
            # if not os.path.exists(model_path):
            #     print(11111111111111111111)
            #     raise ValueError(model_path)
            # print(22222222222222222222222222222)
            model, preprocess = clip.load("ViT-B/32", device=device)
        else:
            raise NotImplementedError(self.feature_type)
        model.eval()

        feats_list = []
        for idx in indices:
            # when error occurs might fail silently when run from torch data parallel
            try:
                feats_dict = self.extract(device, model, preprocess, self.path_list[idx])
                if self.external_call is False:
                    action_on_extraction(feats_dict, self.path_list[idx], self.output_path,
                                         self.on_extraction, self.output_direct)
                else:
                    feats_list.append(feats_dict)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except Exception as e:
                # prints only the last line of an error. Use `traceback.print_exc()` for the whole traceback
                print(e)
                print(f'Extraction failed at: {self.path_list[idx]} with error (↑). Continuing extraction')
                traceback.print_exc()

            # update tqdm progress bar
            self.progress.update()
        return feats_list

    def extract(self, device: torch.device, model: torch.nn.Module,
                preprocess_func, video_path=None):
        """The extraction call. Made to clean the forward call a bit.
           Note that this function won't generate any tmp files

        Arguments:
            device {torch.device}
            model {torch.nn.Module}

        Keyword Arguments:
            video_path {Union[str, None]} -- if you would like to use import it and use it as
                                             "path -> model"-fashion (default: {None})

        Returns:
            Dict[str, np.ndarray]: 'features_nme', 'fps', 'timestamps_ms'
        """

        def _process_frame(frame):
            # frame = video.get_frame(frame)
            if frame is None:
                return None
            frame = Image.fromarray(frame)
            frame = preprocess_func(frame)  # C H W
            return frame

        print("*******",video_path)
        frames, fps, timestamps_ms = extract_frames(str(video_path), self.extract_method)
        # video = mmcv.VideoReader(str(video_path))  # H W C
        # fps, frame_cnt = video.fps, video.frame_cnt
        # mspf = 0.001 / fps  # ms per frame
        #
        # assert self.extraction_fps is not None
        # samples_num = int(frame_cnt / fps * self.extraction_fps)  # get num of sample frame to be extracted
        # samples_ix = np.linspace(1, frame_cnt - 2, samples_num).astype(int)  # 开头结尾两帧可能怪怪的会返回None
        # timestamps_ms = [i * mspf for i in samples_ix]

        frames = [i for i in map(lambda x: _process_frame(x), frames) if i is not None]
        frames = torch.stack(frames).to(device)  # T C H W
        with torch.no_grad():
            features = model.encode_image(frames)  # T E

        features_with_meta = {
            self.feature_type: features.cpu().numpy(),
            'fps': np.array(fps),
            'timestamps_ms': np.array(timestamps_ms)
        }
        return features_with_meta
