from transformers import CLIPImageProcessor
from PIL import Image

# 加载本地图像
image_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\car.jpg"
image = Image.open(image_path)

# 自定义初始化 CLIPImageProcessor
processor = CLIPImageProcessor(
    do_resize=True,
    do_center_crop=True,
    crop_size={"height": 336, "width": 336},  # 裁剪为 224x224
    do_normalize=True,
    image_mean=[0.48145466, 0.4578275, 0.40821073],
    image_std=[0.26862954, 0.26130258, 0.27577711]
)

# 处理图像，返回 tensor
processed_image = processor(images=image, return_tensors="pt")

# 输出图像的尺寸
print(processed_image['pixel_values'].shape)

#%%
from transformers import CLIPImageProcessor
from PIL import Image
import torch
import numpy as np

# 加载本地图像
image_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\car.jpg"
image = Image.open(image_path)

# 初始化处理器
processor = CLIPImageProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 处理图像，返回 tensor
processed_image = processor(images=image, return_tensors="pt")['pixel_values']
print(processed_image.shape)
# 将 PyTorch tensor 转换为 NumPy 数组
processed_image_np = processed_image.squeeze().permute(1, 2, 0).numpy()

# 反归一化图像，以便转换为可视化的图像
mean = np.array([0.48145466, 0.4578275, 0.40821073])
std = np.array([0.26862954, 0.26130258, 0.27577711])
processed_image_np = (processed_image_np * std + mean) * 255
processed_image_np = np.clip(processed_image_np, 0, 255).astype(np.uint8)

# 将 NumPy 数组转换回 PIL Image
processed_image_pil = Image.fromarray(processed_image_np)

# 保存图像
output_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\processed_car.jpg"
processed_image_pil.save(output_path)

print(f"Processed image saved at: {output_path}")

#%%
from transformers import CLIPImageProcessor
from PIL import Image
import torch
import numpy as np

# 加载本地图像
image_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\car.jpg"
image = Image.open(image_path)

# 初始化处理器，不进行裁剪，仅进行缩放
processor = CLIPImageProcessor(
    do_resize=True,  # 只缩放，不裁剪
    size={"height": 224, "width": 224},  # 缩放至224x224大小
    do_center_crop=False,  # 禁用中心裁剪
    do_normalize=True,
    image_mean=[0.48145466, 0.4578275, 0.40821073],
    image_std=[0.26862954, 0.26130258, 0.27577711]
)

# 处理图像，返回 tensor
processed_image = processor(images=image, return_tensors="pt")['pixel_values']
print(processed_image.shape)

# 将 PyTorch tensor 转换为 NumPy 数组
processed_image_np = processed_image.squeeze().permute(1, 2, 0).numpy()

# 反归一化图像，以便转换为可视化的图像
mean = np.array([0.48145466, 0.4578275, 0.40821073])
std = np.array([0.26862954, 0.26130258, 0.27577711])
processed_image_np = (processed_image_np * std + mean) * 255
processed_image_np = np.clip(processed_image_np, 0, 255).astype(np.uint8)

# 将 NumPy 数组转换回 PIL Image
processed_image_pil = Image.fromarray(processed_image_np)

# 保存图像
output_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\processed_car_no_crop.jpg"
processed_image_pil.save(output_path)

print(f"Processed image saved at: {output_path}")

#%%
from transformers import CLIPImageProcessor
from PIL import Image
import torch
import numpy as np

# 加载本地图像
image_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\car.jpg"
image = Image.open(image_path)

# 显式使用 CLIPImageProcessor 初始化处理器
processor = CLIPImageProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 处理图像，返回 PyTorch tensor。这里明确指定 'return_tensors' 参数为 'pt' 以获取 PyTorch 格式
processed_image = processor(images=image, return_tensors="pt")['pixel_values']
print(f"Processed image tensor shape: {processed_image.shape}")

# 将 PyTorch tensor 转换为 NumPy 数组，注意要先移除 batch 维度 (squeeze) 再转置轴 (permute)
processed_image_np = processed_image.squeeze().permute(1, 2, 0).numpy()

# 使用 CLIP 的均值和标准差进行反归一化，以便转换为可视化的图像
mean = np.array([0.48145466, 0.4578275, 0.40821073])
std = np.array([0.26862954, 0.26130258, 0.27577711])
# 反归一化处理：乘以标准差再加回均值，并乘以 255 以转换为标准 RGB 范围
processed_image_np = (processed_image_np * std + mean) * 255
# 使用 np.clip 确保像素值在 0 到 255 之间，并转换为 uint8 类型
processed_image_np = np.clip(processed_image_np, 0, 255).astype(np.uint8)

# 将 NumPy 数组转换回 PIL Image 以便保存或进一步操作
processed_image_pil = Image.fromarray(processed_image_np)

# 保存处理后的图像到指定路径
output_path = r"C:\Users\Administrator\PycharmProjects\code_res\image\processed_car336_new.jpg"
processed_image_pil.save(output_path)

print(f"Processed image saved at: {output_path}")
