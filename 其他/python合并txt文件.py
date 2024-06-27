import os
import glob

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)

# 指定文件夹路径
folder_path = r'C:\Users\Administrator\Downloads\VBench-master\VBench-master\prompts\prompts_per_dimension'

# 创建一个新的文件，用于存储合并后的内容
with open('merged_file.txt', 'w', encoding='utf-8') as outfile:
    total_lines = 0
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        file_lines = count_lines(filename)
        total_lines += file_lines
        with open(filename, 'r', encoding='utf-8') as readfile:
            outfile.write(readfile.read())
            outfile.write('\n')  # 确保每个文件的内容后添加一个换行符

# 计算合并后的文件行数
merged_lines = count_lines('merged_file.txt')

print(f"所有txt文件已合并到 merged_file.txt，总行数: {merged_lines}")
print(f"预期总行数: {total_lines}")

# 验证合并后的行数是否与预期一致
if merged_lines == total_lines:
    print("合并后的文件行数正确")
else:
    print(f"警告: 合并后的文件行数 ({merged_lines}) 与预期的行数 ({total_lines}) 不一致")
