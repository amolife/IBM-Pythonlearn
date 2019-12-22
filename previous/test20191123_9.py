import numpy as np
import matplotlib.pyplot as plt

# 先生成画布
fig = plt.figure()

x = np.random.randn(100)
y = np.random.randn(100)
# colors = np.random.rand(100)

sizes = np.random.rand(100) * 300

# alpha 指定点的透明度，默认是1
# 之前的颜色使用 color 参数，指定一样的颜色。
# 这里是c，指定一个和元素一样长的数组，下面的做法是为每个点换一个颜色，依次过度
plt.scatter(x, y, c=[i for i in range(100)], s=sizes, alpha=0.6)
plt.colorbar()  # 显示右边的颜色的数值条
#plt.legend()
# 展示图像
plt.show()


# 保存到文件
fig.savefig("test3.png")  # 保存为png