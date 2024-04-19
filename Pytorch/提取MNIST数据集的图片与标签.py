import os
import torch
from torchvision import datasets, transforms
from PIL import Image

# 加载MNIST数据集，这次不应用任何转换，因为默认返回的就是PIL Image
mnist_train = datasets.MNIST(root='./MNIST_data/', train=True, download=True)
mnist_test = datasets.MNIST(root='./MNIST_data/', train=False, download=True)

# 定义保存图片和标签的目录
image_dir = 'mnist_images'
label_dir = 'mnist_labels'

# 确保保存目录存在
os.makedirs(image_dir, exist_ok=True)
os.makedirs(label_dir, exist_ok=True)

# 遍历训练数据集并保存图片和标签
for idx, (image, label) in enumerate(mnist_train):
    # 保存图片
    image_path = os.path.join(image_dir, f'{idx:05d}.png')  # 使用5位数序号命名图片文件
    image.save(image_path)

    # 保存标签
    label_path = os.path.join(label_dir, f'{idx:05d}.txt')
    with open(label_path, 'w') as f:
        f.write(f'{idx:05d} {label}\n')  # 文件内容是图片序号和对应标签

# 遍历测试数据集并保存图片和标签
for idx, (image, label) in enumerate(mnist_test, start=len(mnist_train)):
    # 保存图片
    image_path = os.path.join(image_dir, f'{idx:05d}.png')  # 使用5位数序号命名图片文件
    image.save(image_path)

    # 保存标签
    label_path = os.path.join(label_dir, f'{idx:05d}.txt')
    with open(label_path, 'w') as f:
        f.write(f'{idx:05d} {label}\n')  # 文件内容是图片序号和对应标签

print("图片和标签保存完成！")