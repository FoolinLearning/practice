# 引入必要的库
import torch
import torch.nn as nn
import numpy

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]
x_tensor = torch.tensor(x)
y_tensor = torch.tensor(y)
# 将转换成的tensor变量转换成floattensor类型，并传入GPU
x_tensor = x_tensor.float().cuda() 
y_tensor = y_tensor.float().cuda()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

my_Net = nn.Sequential(
    nn.Linear(2, 20),
    nn.ReLU(),          #ReLU激活函数
    nn.Linear(20, 1),
    nn.Sigmoid()
)                 #搭建网络模型，传入GPU

my_Net.to(device) #直接使用.cude不可以，原因可能是这不是一个实例

# print(my_Net) for test

# 构建优化器
# 格式为：
# 优化器名 = torch.optim.优化器接口(网络名.parameters, 其他参数)`

optimizer = torch.optim.SGD(my_Net.parameters(), lr= 0.05)

#损失函数的设置，这部分应该是固定格式,使用MSE进行损失函数的计算
#
loss_func = nn.MSELoss()

#训练部分
for epoch in range(5000): #完整训练5000次完整的训练集
    out = my_Net(x_tensor) #输入一次x，得到实际的输入,并不是广义上的输出
    loss = loss_func(out, y_tensor)   #传入实际输出与期望输出，得到损失函数
    optimizer.zero_grad()  #清除之前的梯度，每进行一次优化就要清除之前的梯度
    loss.backward()   #误差的反向传播
    optimizer.step()  #优化器开始优化
    if epoch % 1000 == 0:
        print(f'迭代次数:{epoch}')
        print(f'误差:{loss}')

out = my_Net(x_tensor).detach().cpu()  #最后一次的输入传入cpu
print(f'out:{out.numpy()}')

torch.save(my_Net, 'C:/Users/Hk/Desktop/github/practice/net.pkl')  #把训练好的网络保存到文件里

