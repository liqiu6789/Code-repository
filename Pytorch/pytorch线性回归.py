import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 生成随机数据
x_train = np.random.rand(100, 1) * 10  # 100个样本，每个样本1个特征，值在0到10之间
y_train = 2 * x_train + 3 + np.random.randn(100, 1) * 0.5  # 线性关系加上一些噪声

# 将numpy数组转换为torch张量
x_train = torch.from_numpy(x_train).float()
y_train = torch.from_numpy(y_train).float()


# 定义模型
class LinearRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        out = self.linear(x)
        return out

    # 初始化模型


input_dim = x_train.shape[1]
output_dim = 1
model = LinearRegressionModel(input_dim, output_dim)

# 定义损失函数和优化器
criterion = nn.MSELoss()  # 均方误差损失函数
learning_rate = 0.01
optimizer = optim.SGD(model.parameters(), lr=learning_rate)  # 随机梯度下降优化器

# 训练模型
num_epochs = 1000
for epoch in range(num_epochs):
    # 前向传播
    outputs = model(x_train)
    loss = criterion(outputs, y_train)

    # 反向传播和优化
    optimizer.zero_grad()  # 清空梯度缓存
    loss.backward()  # 反向传播，计算当前梯度
    optimizer.step()  # 根据梯度更新权重

    # 每100个epoch打印一次损失值
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    # 预测
with torch.no_grad():  # 不需要计算梯度
    predictions = model(x_train)
    print(predictions)