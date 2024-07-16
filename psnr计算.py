import os
import cv2
import torch
import argparse
import numpy as np
from tqdm import tqdm
from torch.nn import functional as F
import warnings
import skvideo.io
from queue import Queue, Empty
from model.pytorch_msssim import ssim_matlab

warnings.filterwarnings("ignore")


def transferAudio(sourceVideo, targetVideo):
    import shutil
    import moviepy.editor
    tempAudioFileName = "./temp/audio.mkv"

    if os.path.isdir("temp"):
        shutil.rmtree("temp")
    os.makedirs("temp")

    os.system(f'ffmpeg -y -i "{sourceVideo}" -c:a copy -vn {tempAudioFileName}')

    targetNoAudio = os.path.splitext(targetVideo)[0] + "_noaudio" + os.path.splitext(targetVideo)[1]
    os.rename(targetVideo, targetNoAudio)
    os.system(f'ffmpeg -y -i "{targetNoAudio}" -i {tempAudioFileName} -c copy "{targetVideo}"')

    if os.path.getsize(targetVideo) == 0:
        tempAudioFileName = "./temp/audio.m4a"
        os.system(f'ffmpeg -y -i "{sourceVideo}" -c:a aac -b:a 160k -vn {tempAudioFileName}')
        os.system(f'ffmpeg -y -i "{targetNoAudio}" -i {tempAudioFileName} -c copy "{targetVideo}"')
        if os.path.getsize(targetVideo) == 0:
            os.rename(targetNoAudio, targetVideo)
            print("音频转移失败。插值视频将没有音频")
        else:
            print("无损音频转移失败。音频已转码为AAC (M4A)。")
            os.remove(targetNoAudio)
    else:
        os.remove(targetNoAudio)
    shutil.rmtree("temp")


parser = argparse.ArgumentParser(description='图像对的插值')
parser.add_argument('--video', dest='video', type=str, default=None)
parser.add_argument('--output', dest='output', type=str, default=None)
parser.add_argument('--img', dest='img', type=str, default=None)
parser.add_argument('--montage', dest='montage', action='store_true', help='蒙太奇原始视频')
parser.add_argument('--model', dest='modelDir', type=str, default='train_log', help='训练模型文件目录')
parser.add_argument('--fp16', dest='fp16', action='store_true',
                    help='在具有张量核心的卡上使用fp16模式以更快和更轻量的推理')
parser.add_argument('--UHD', dest='UHD', action='store_true', help='支持4k视频')
parser.add_argument('--scale', dest='scale', type=float, default=1.0, help='尝试scale=0.5用于4k视频')
parser.add_argument('--skip', dest='skip', action='store_true', help='处理前是否移除静态帧')
parser.add_argument('--fps', dest='fps', type=int, default=None)
parser.add_argument('--png', dest='png', action='store_true', help='是否输出png格式')
parser.add_argument('--ext', dest='ext', type=str, default='mp4', help='输出视频格式')
parser.add_argument('--exp', dest='exp', type=int, default=1)
args = parser.parse_args()
assert args.video is not None or args.img is not None, "必须指定--video或--img"

if args.skip:
    print("skip标志已废弃，请参阅问题#207。")
if args.UHD and args.scale == 1.0:
    args.scale = 0.5
assert args.scale in [0.25, 0.5, 1.0, 2.0, 4.0]
if args.img is not None:
    args.png = True

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.set_grad_enabled(False)
if torch.cuda.is_available():
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True
    if args.fp16:
        torch.set_default_tensor_type(torch.cuda.HalfTensor)

try:
    try:
        from model.RIFE_HDv2 import Model

        model = Model()
        model.load_model(args.modelDir, -1)
        print("已加载v2.x HD模型。")
    except:
        from train_log.RIFE_HDv3 import Model

        model = Model()
        model.load_model(args.modelDir, -1)
        print("已加载v3.x HD模型。")
except:
    from model.RIFE_HD import Model

    model = Model()
    model.load_model(args.modelDir, -1)
    print("已加载v1.x HD模型")

model.eval()
model.device()

if args.video is not None:
    videoCapture = cv2.VideoCapture(args.video)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    tot_frame = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    videoCapture.release()
    if args.fps is None:
        fpsNotAssigned = True
        args.fps = fps * (2 ** args.exp)
    else:
        fpsNotAssigned = False
    videogen = skvideo.io.vreader(args.video)
    lastframe = next(videogen)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video_path_wo_ext, ext = os.path.splitext(args.video)
    print(f'{video_path_wo_ext}.{args.ext}, {tot_frame}帧总数，从{fps}FPS到{args.fps}FPS')
    if not args.png and fpsNotAssigned:
        print("音频将在插值过程后合并")
    else:
        print("由于使用了png或fps标志，不会合并音频！")
else:
    videogen = []
    for f in os.listdir(args.img):
        if 'png' in f:
            videogen.append(f)
    tot_frame = len(videogen)
    videogen.sort(key=lambda x: int(x[:-4]))
    lastframe = cv2.imread(os.path.join(args.img, videogen[0]), cv2.IMREAD_UNCHANGED)[:, :, ::-1].copy()
    videogen = videogen[1:]

h, w, _ = lastframe.shape
vid_out_name = None
vid_out = None
if args.png:
    if not os.path.exists('vid_out'):
        os.mkdir('vid_out')
else:
    if args.output is not None:
        vid_out_name = args.output
    else:
        vid_out_name = f'{video_path_wo_ext}_{2 ** args.exp}X_{int(np.round(args.fps))}fps.{args.ext}'
    vid_out = cv2.VideoWriter(vid_out_name, fourcc, args.fps, (w, h))


def make_inference(I0, I1, n):
    global model
    middle = model.inference(I0, I1, args.scale)
    if n == 1:
        return [middle]
    first_half = make_inference(I0, middle, n=n // 2)
    second_half = make_inference(middle, I1, n=n // 2)
    if n % 2:
        return [*first_half, middle, *second_half]
    else:
        return [*first_half, *second_half]


def pad_image(img):
    if args.fp16:
        return F.pad(img, padding).half()
    else:
        return F.pad(img, padding)


if args.montage:
    left = w // 4
    w = w // 2
tmp = max(32, int(32 / args.scale))
ph = ((h - 1) // tmp + 1) * tmp
pw = ((w - 1) // tmp + 1) * tmp
padding = (0, pw - w, 0, ph - h)
pbar = tqdm(total=tot_frame)
if args.montage:
    lastframe = lastframe[:, left: left + w]

write_buffer = Queue(maxsize=500)
read_buffer = Queue(maxsize=500)


def process_frames(videogen, write_buffer, read_buffer):
    I1 = torch.from_numpy(np.transpose(lastframe, (2, 0, 1))).to(device, non_blocking=True).unsqueeze(0).float() / 255.
    I1 = pad_image(I1)
    temp = None  # save lastframe when processing static frame

    for frame in videogen:
        if args.img is not None:
            frame = cv2.imread(os.path.join(args.img, frame), cv2.IMREAD_UNCHANGED)[:, :, ::-1].copy()
        if args.montage:
            frame = frame[:, left: left + w]
        read_buffer.put(frame)

    read_buffer.put(None)

    while True:
        if temp is not None:
            frame = temp
            temp = None
        else:
            frame = read_buffer.get()
        if frame is None:
            break
        I0 = I1
        I1 = torch.from_numpy(np.transpose(frame, (2, 0, 1))).to(device, non_blocking=True).unsqueeze(0).float() / 255.
        I1 = pad_image(I1)
        I0_small = F.interpolate(I0, (32, 32), mode='bilinear', align_corners=False)
        I1_small = F.interpolate(I1, (32, 32), mode='bilinear', align_corners=False)
        ssim = ssim_matlab(I0_small[:, :3], I1_small[:, :3])

        break_flag = False
        if ssim > 0.996:
            frame = read_buffer.get()  # read a new frame
            if frame is None:
                break_flag = True
                frame = lastframe
            else:
                temp = frame
            I1 = torch.from_numpy(np.transpose(frame, (2, 0, 1))).to(device, non_blocking=True).unsqueeze(
                0).float() / 255.
            I1 = pad_image(I1)
            I1 = model.inference(I0, I1, args.scale)
            I1_small = F.interpolate(I1, (32, 32), mode='bilinear', align_corners=False)
            ssim = ssim_matlab(I0_small[:, :3], I1_small[:, :3])
            frame = (I1[0] * 255).byte().cpu().numpy().transpose(1, 2, 0)[:h, :w]

        if ssim < 0.2:
            output = []
            for i in range((2 ** args.exp) - 1):
                output.append(I0)
        else:
            output = make_inference(I0, I1, 2 ** args.exp - 1) if args.exp else []

        if args.montage:
            write_buffer.put(np.concatenate((lastframe, lastframe), 1))
            for mid in output:
                mid = (((mid[0] * 255.).byte().cpu().numpy().transpose(1, 2, 0)))
                write_buffer.put(np.concatenate((lastframe, mid[:h, :w]), 1))
        else:
            write_buffer.put(lastframe)
            for mid in output:
                mid = (((mid[0] * 255.).byte().cpu().numpy().transpose(1, 2, 0)))
                write_buffer.put(mid[:h, :w])
        pbar.update(1)
        lastframe = frame
        if break_flag:
            break

    if args.montage:
        write_buffer.put(np.concatenate((lastframe, lastframe), 1))
    else:
        write_buffer.put(lastframe)


process_frames(videogen, write_buffer, read_buffer)

pbar.close()
if vid_out is not None:
    while not write_buffer.empty():
        frame = write_buffer.get()
        if frame is not None:
            vid_out.write(frame[:, :, ::-1])
    vid_out.release()

# move audio to new video file if appropriate
if not args.png and fpsNotAssigned and args.video is not None:
    try:
        transferAudio(args.video, vid_out_name)
    except Exception as e:
        print(f"音频转移失败。插值视频将没有音频: {e}")
        targetNoAudio = os.path.splitext(vid_out_name)[0] + "_noaudio" + os.path.splitext(vid_out_name)[1]
        os.rename(targetNoAudio, vid_out_name)
