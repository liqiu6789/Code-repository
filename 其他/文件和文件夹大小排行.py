import os
from collections import defaultdict
import stat

def get_size(start_path='.'):
    """
    递归获取文件夹及其子文件夹和文件的大小（以MB为单位）
    """
    total_size_bytes = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 跳过如果它是符号链接
            if not os.path.islink(fp):
                total_size_bytes += os.path.getsize(fp)
                # 将字节转换为MB
    total_size_mb = total_size_bytes / (1024 * 1024)
    return total_size_mb


def list_files_and_folders(start_path='.'):
    """
    列出文件夹及其子文件夹和文件的大小，并返回字典（以MB为单位）
    """
    sizes = defaultdict(float)

    for dirpath, dirnames, filenames in os.walk(start_path):
        # 排除隐藏的子文件夹
        dirnames[:] = [d for d in dirnames if
                       not os.stat(os.path.join(dirpath, d)).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN]

        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 跳过如果它是符号链接或隐藏文件
            if not os.path.islink(fp) and not os.stat(fp).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN:
                sizes[fp] = os.path.getsize(fp) / (1024 * 1024)  # 直接转换为MB

        for d in dirnames:
            dp = os.path.join(dirpath, d)
            # 计算子文件夹的大小（以MB为单位），并将其添加到sizes字典中
            sizes[dp] = get_size(dp)

    return sizes


def rank_sizes(sizes):
    """
    根据大小对文件/文件夹进行排名
    """
    return sorted(sizes.items(), key=lambda x: x[1], reverse=True)


def print_ranked_sizes(ranked_sizes, output_file='ranked_sizes.txt'):
    """
    打印排名后的文件/文件夹大小（以MB为单位）并保存到文件
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for rank, (path, size) in enumerate(ranked_sizes, start=1):
            # 打印到控制台
            print(f"Rank {rank}: {path} - {size:.2f} MB")
            # 写入到文件
            f.write(f"Rank {rank}: {path} - {size:.2f} MB\n")



if __name__ == "__main__":
    start_path = "C:\Program Files (x86)"
    sizes = list_files_and_folders(start_path)
    ranked_sizes = rank_sizes(sizes)
    print_ranked_sizes(ranked_sizes, output_file='ranked_sizes.txt')
