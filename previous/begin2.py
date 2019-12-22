
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib as mpl

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
np.set_printoptions(threshold=sys.maxsize)


fig, axes = plt.subplots(2,2)

axes[0,1].set_title = ("第一图")



plt.show()
