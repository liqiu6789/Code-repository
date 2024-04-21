# 保存模型权重
torch.save(model.state_dict(), 'model_weights.pth')
# 保存整个模型（包括结构和权重）
torch.save(model, 'model.pth')
# 加载整个模型
loaded_model = torch.load('model.pth')