from PIL import Image
import os


def gif_to_images(gif_path, output_folder):
    # 打开 GIF 文件
    gif = Image.open(gif_path)

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取 GIF 的帧数
    frame_count = gif.n_frames

    for frame in range(frame_count):
        # 设置当前帧
        gif.seek(frame)

        # 将当前帧保存为图像
        frame_image_path = os.path.join(output_folder, f"frame_{frame}.png")
        gif.save(frame_image_path, "PNG")
        print(f"Saved {frame_image_path}")


if __name__ == "__main__":
    gif_path = "QTQBAP2Q.gif"  # 替换为你的 GIF 文件路径
    output_folder = "gif_png"  # 替换为你想保存帧图片的文件夹路径

    gif_to_images(gif_path, output_folder)
