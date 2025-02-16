import pandas as pd
import random

# 定义英雄列表
heroes = ["刘备", "关羽", "张飞", "孙尚香", "曹操"]

# 初始化空的数据列表
data = []

# 生成100行数据
for _ in range(100):
    # 随机选择两个不同的英雄
    hero1, hero2 = random.sample(heroes, 2)

    # 随机生成0-9之间的分数
    score1 = random.randint(0, 9)
    score2 = random.randint(0, 9)

    # 将数据添加到列表中
    data.append([hero1, score1, hero2, score2])

# 创建 DataFrame
columns = ["英雄1", "英雄分数1", "英雄2", "英雄分数2"]
df = pd.DataFrame(data, columns=columns)

# 将 DataFrame 写入 CSV 文件
df.to_csv("data.csv", index=False, encoding="utf-8")

print("data.csv 文件已成功生成！")