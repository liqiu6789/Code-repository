# video_features

这是一个使用预训练网络提取视频特征的小库，frok自@v-iashin 大佬（感谢！）。

这个repo实现了：

- [x] 多GPU提取视频特征
- [x] 支持模型：CLIP、I3D（使用raft、pwc提取光流图或者使用已有的光流图）
- [x] 也许支持但未验证的：r21D、vggish、resnet（这一部分是原repo中实现的，可以移步至另一边，由于我的魔改也许破坏了一些东西）
- [x] 相较于原repo，输入输出的方式更多（命令行参数输入、文件输入、视频目录输入、npy数组输出、pkl输出、光流图片输出）
- [x] 支持外部调用，如我在[另一个repo](https://github.com/Kamino666/Video-Captioning-Transformer/blob/dev/predict_video.py)中实现的那样。

## 使用方法

### 批量提取CLIP特征

先根据[CLIP](http://proceedings.mlr.press/v139/radford21a)的教程配置好环境，下面的这几种参数是必填的：

```bash
python main.py 
--feature_type CLIP-ViT-B/32 \    # 特征种类
--output_direct                   # 填上吧
--device_ids 0 1 2 3 或者 --cpu \  # 使用GPU或者CPU提取
--on_extraction save_numpy \      # 保存方式，推荐以npy数组保存
--extract_method uni_12 \      # 抽帧方式 uni_12表示等间隔抽12帧 fix_2表示以fps2抽帧
--video_dir 或者 --video_paths \   # 视频输入方式 
--output_path                     # 输出目录
```

下面的命令使用`CLIP-ViT-B/32`模型，用cpu以抽取12帧的方式提取了一个视频的特征，输出结果npy数组保存在sample下。

```bash
python main.py --feature_type CLIP-ViT-B/32 --output_direct --cpu --on_extraction save_numpy --extract_method uni_12 --video_paths ./sample/v_GGSY1Qvo990.mp4 --output_path ./sample
```

### 外部调用提取CLIP特征

```python
def extract_feat(args):
    # 把一些attribute填在一个空对象里面
    # useful attributes
    args.extract_method = args.ext_type
    args.feature_type = args.feat_type[0]
    args.video_paths = [args.video]
    # useless attribute
    args.extraction_fps = None
    args.file_with_video_paths = None
    args.flow_dir = None
    args.flow_paths = None
    args.video_dir = None
    args.on_extraction = None
	# 导入特征提取类
    from submodules.video_features.models.CLIP.extract_clip import ExtractCLIP
    extractor = ExtractCLIP(args, external_call=True)  # 指定外部调用为True
    feats_list = extractor(torch.zeros([1], dtype=torch.long))[0][args.feature_type]
    feats_list = torch.from_numpy(feats_list).unsqueeze(0)
```

### 批量提取I3D特征

和CLIP差不多，但是要指定提取光流的方法`flow_type`。

```bash
python main.py \
--feature_type i3d --flow_type raft \
--output_direct --cpu --on_extraction save_numpy \
--video_paths ./sample/v_GGSY1Qvo990.mp4 --output_path ./sample
```



下面是原库的README

# Extract Video Features Using Multiple GPUs

This is the source code for `video_features`, a small library that allows you to extract features from raw videos using the pre-trained nets. So far, it supports several extractors that capture visual appearance, calculates optical flow, and, even, audio features.

The source code was intended to support the feature extraction pipeline for two of my papers ([BMT](https://arxiv.org/abs/2005.08271) and [MDVC](https://arxiv.org/abs/2003.07758)). This small library somehow emerged out of that code and now has more models implemented.

### [Documentation is here](https://iashin.ai/video_features/)
