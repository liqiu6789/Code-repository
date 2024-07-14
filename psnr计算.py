import os
import cv2
import numpy as np


def calculate_psnr(video1_path, video2_path):
    cap1 = cv2.VideoCapture(video1_path)  # 打开第一个视频文件
    cap2 = cv2.VideoCapture(video2_path)  # 打开第二个视频文件

    psnr_values = []  # 初始化用于存储PSNR值的列表
    frame_count = 0  # 初始化帧计数器

    while True:
        ret1, frame1 = cap1.read()  # 读取第一个视频的下一帧
        ret2, frame2 = cap2.read()  # 读取第二个视频的下一帧

        if not ret1:  # 如果第一个视频到达结尾，则退出循环
            break

        if frame_count % 2 == 0:  # 只在第二个视频每隔一帧进行读取
            if not ret2:
                break  # 如果第二个视频到达结尾，则退出循环
            frame2 = cap2.read()[1]  # 读取第二个视频的下一帧

        psnr_value = cv2.PSNR(frame1, frame2)  # 计算当前帧的PSNR值
        psnr_values.append(psnr_value)  # 将PSNR值添加到列表中

        frame_count += 1  # 增加帧计数器

    cap1.release()  # 释放第一个视频资源
    cap2.release()  # 释放第二个视频资源

    if psnr_values:  # 如果有PSNR值，则返回它们的平均值
        return np.mean(psnr_values)
    else:  # 如果没有PSNR值，返回None
        return None


def get_video_files(folder):
    # 定义获取文件夹中所有视频文件的函数
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']  # 定义支持的视频文件扩展名
    return [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in video_extensions]
    # 返回文件夹中所有符合扩展名的视频文件名列表


def main(folder1, folder2):
    # 定义主函数，计算两个文件夹中对应视频的PSNR值
    videos1 = get_video_files(folder1)  # 获取第一个文件夹中的视频文件
    videos2 = get_video_files(folder2)  # 获取第二个文件夹中的视频文件

    common_videos = set(videos1).intersection(videos2)  # 找出两个文件夹中共有的视频文件

    psnr_results = {}  # 初始化用于存储PSNR结果的字典

    for video in common_videos:  # 对每一个共有的视频文件进行处理
        video1_path = os.path.join(folder1, video)  # 获取第一个文件夹中视频的完整路径
        video2_path = os.path.join(folder2, video)  # 获取第二个文件夹中视频的完整路径
        psnr_value = calculate_psnr(video1_path, video2_path)  # 计算视频之间的PSNR值
        psnr_results[video] = psnr_value  # 将结果存储在字典中

    return psnr_results  # 返回PSNR结果字典


# 示例用法
folder1 = 'path_to_first_video_folder'  # 第一个视频文件夹路径
folder2 = 'path_to_second_video_folder'  # 第二个视频文件夹路径
results = main(folder1, folder2)  # 调用主函数计算PSNR

for video, psnr in results.items():  # 打印每个视频的PSNR值
    print(f"PSNR for {video}: {psnr} dB")
