import base64
import wave
import os


def audio_to_base64(audio_file_path, output_txt_path):
    # 打开音频文件
    with wave.open(audio_file_path, 'rb') as audio_file:
        # 读取二进制数据
        audio_content = audio_file.readframes(audio_file.getnframes())

        # 将二进制数据编码为Base64
    base64_content = base64.b64encode(audio_content).decode('utf-8')

    # 将Base64编码保存到文本文件
    with open(output_txt_path, 'w') as txt_file:
        txt_file.write(base64_content)

    print(f"音频文件已成功转换为Base64并保存到 {output_txt_path}")


def base64_to_audio(base64_txt_path, output_audio_path, original_audio_path):
    # 从文本文件读取Base64编码
    with open(base64_txt_path, 'r') as txt_file:
        base64_content = txt_file.read()

        # 将Base64编码解码为二进制数据
    audio_content = base64.b64decode(base64_content)

    # 读取原始音频文件的参数
    with wave.open(original_audio_path, 'rb') as original_audio_file:
        params = original_audio_file.getparams()

        # 创建一个新的wave文件对象并写入二进制数据，使用原始音频文件的参数
    with wave.open(output_audio_path, 'wb') as audio_file:
        audio_file.setparams(params)
        audio_file.writeframes(audio_content)

    print(f"Base64编码已成功还原为音频文件并保存到 {output_audio_path}")


# 使用函数示例
audio_file = 'example.wav'  # 假设当前目录有一个名为example.wav的音频文件
base64_txt = 'base64.txt'  # 输出的Base64编码文本文件名

# 将音频文件转换为Base64并保存为文本文件
audio_to_base64(audio_file, base64_txt)

# 从Base64编码文本文件还原为音频文件
output_audio = 'restored_example.wav'  # 还原后的音频文件名
base64_to_audio(base64_txt, output_audio,audio_file)