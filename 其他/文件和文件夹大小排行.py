import os
from collections import defaultdict


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
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 跳过如果它是符号链接
            if not os.path.islink(fp):
                sizes[fp] += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            sizes[dp] = get_size(dp)
            # 将所有大小转换为MB
    for path in sizes:
        sizes[path] /= (1024 * 1024)
    return sizes


def rank_sizes(sizes):
    """
    根据大小对文件/文件夹进行排名
    """
    return sorted(sizes.items(), key=lambda x: x[1], reverse=True)


def print_ranked_sizes(ranked_sizes, output_file='ranked_sizes.txt'):
    """
    打印排名后的文件/文件夹大小（以MB为单位）
    """
    for rank, (path, size) in enumerate(ranked_sizes, start=1):
        print(f"Rank {rank}: {path} - {size:.2f} MB")  # 使用:.2f来保留两位小数
        with open(output_file, 'w', encoding='utf-8') as f:
            for rank, (path, size) in enumerate(ranked_sizes, start=1):
                # 打印到控制台
                print(f"Rank {rank}: {path} - {size:.2f} MB")
                # 写入到文件
                f.write(f"Rank {rank}: {path} - {size:.2f} MB\n")


if __name__ == "__main__":
    start_path = r"C:\BaiduNetdiskDownload"
    sizes = list_files_and_folders(start_path)
    ranked_sizes = rank_sizes(sizes)
    print_ranked_sizes(ranked_sizes)
