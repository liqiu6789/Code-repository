import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# 创建示例任务数据
data = {
    'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
    'Start': ['2023-07-01', '2023-07-05', '2023-07-10', '2023-07-15'],
    'End': ['2023-07-10', '2023-07-15', '2023-07-20', '2023-07-25']
}

# 转换为DataFrame
df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# 绘制甘特图
fig, ax = plt.subplots(figsize=(10, 5))

# 将任务按结束时间排序，确保绘图时任务从上到下排列
df = df.sort_values(by='End')

# 绘制每个任务的条形
for i, task in enumerate(df.itertuples()):
    ax.barh(task.Task, (task.End - task.Start).days, left=task.Start)

# 设置x轴的日期格式
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# 设置图表标题和标签
plt.title('Gantt Chart')
plt.xlabel('Date')
plt.ylabel('Task')

# 自动旋转日期标签
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
