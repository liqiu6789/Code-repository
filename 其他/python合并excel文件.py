import os
import pandas as pd


def merge_excel_files_in_folder(folder_path, output_filename):
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    all_data = []

    # 遍历所有文件并读取数据
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path, index_col=None, header=0)
        all_data.append(df)

        # 合并所有DataFrame
    merged_df = pd.concat(all_data, ignore_index=True)

    # 保存到新的Excel文件
    merged_df.to_excel(output_filename, index=False)


# 使用示例
folder_path = 'excel_files'  # 替换为你的文件夹路径
output_filename = 'merged_output.xlsx'  # 输出的Excel文件名
merge_excel_files_in_folder(folder_path, output_filename)