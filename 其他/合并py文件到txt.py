import os

def merge_py_files(folder_path, output_file):
    # 检查指定的文件夹是否存在
    if not os.path.isdir(folder_path):
        print(f"指定的文件夹不存在: {folder_path}")
        return

    # 打开输出文件（如果不存在则创建）
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍历指定文件夹下的所有文件
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 只处理 .py 文件
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        # 写入文件名作为分隔符
                        outfile.write(f"\n\n# {file}\n")
                        # 读取并写入 .py 文件的内容
                        outfile.write(infile.read())
    print(f"所有 .py 文件已合并到 {output_file}")

# 示例用法
folder_path = r'C:\Users\Administrator\PycharmProjects\code_res\其他\pyqt5-django-app-api-main\pyqt_project'  # 替换为你的文件夹路径
output_file = 'merged_files.txt'  # 替换为你的输出文件路径
merge_py_files(folder_path, output_file)
