import os
import glob

# 指定文件夹路径
folder_path = './txt_files'

# 创建一个新的文件，用于存储合并后的内容
with open('merged_file.txt', 'w', encoding='utf-8') as outfile:
    # 遍历文件夹中的所有txt文件
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        # 打开每个txt文件并读取内容
        with open(filename, 'r', encoding='utf-8') as readfile:
            # 将内容写入到合并后的文件中
            outfile.write(readfile.read() + '\n\n')  # 在每个文件内容后添加两个换行符，以便区分不同的文件内容

print("所有txt文件已合并到 merged_file.txt")