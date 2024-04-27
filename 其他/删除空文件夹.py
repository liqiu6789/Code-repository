import os


def remove_empty_directories(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                # 如果需要记录被删除的目录，可以取消注释下一行
                print(f"Removed empty directory: {dir_path}")


# 在这里指定要检查并删除空文件夹的目录路径
target_directory = "C:\\"  # 替换为您想要检查的目录路径

if os.path.isdir(target_directory):
    remove_empty_directories(target_directory)
else:
    print(f"The path '{target_directory}' is not a valid directory.")