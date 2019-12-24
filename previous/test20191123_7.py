import numpy as np
import matplotlib.pyplot as plt

# 先生成画布
fig = plt.figure()

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,  3 * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin, label="sin(x)")
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2)
plt.plot(x, y_cos, label="cos(x)")
plt.title('Cosine')
plt.legend()
# 展示图像
plt.show()


# 保存到文件
fig.savefig("test2.png")  # 保存为png