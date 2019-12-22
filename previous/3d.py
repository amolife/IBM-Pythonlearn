import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D#需另外导入模块Axes 3D
fig=plt.figure()#定义图像窗口
ax=Axes3D(fig)#在窗口上添加3D坐标轴
#将X和Y值编织成栅格
X=np.arange(-10,10,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)

R=np.sqrt(X**2+Y**2)
Z=np.sin(R)#高度值
#将colormap rainbow填充颜色，之后将三维图像投影到XY平面做等高线图，其中ratride和cstride表示row和column的宽度
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))#rstride表示图像中分割线的跨图
#添加XY平面等高线 投影到z平面
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap=plt.get_cmap('rainbow'))#把图像进行投影的图形 offset表示比0坐标轴低两个位置
ax.set_zlim(-2,2)
plt.show()
print(Z)
