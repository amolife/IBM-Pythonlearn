import numpy as np
import matplotlib.pyplot as plt
import sys

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
np.set_printoptions(threshold=sys.maxsize)

#from matplotlib.font_manager import _rebuild
#_rebuild() #reload一下,中文显示ok了

x = np.random.rand(3,5)
t = np.random.randn(10)
#x = np.array(x)
y = np.linspace(1,10,9,endpoint=False,retstep=False)
# retstep=true, y= tuple; retstep=False,y=array
z = np.random.randint(1,15,size=20)
z1 = np.random.randint(1,15,size=(3,5))
a = np.arange(125).reshape(5,5,5)
a1 = a[1,2,3]
b = np.random.random(10)
b1 =np.square(b)
print('x=',x,'\n'
      'y=',y,'\n'
      't=',t,'\n'
      'z=',z,'\n'
      'z1=',z1,'\n'
      'a=',a,'\n'
      'a1=',a1,'\n'
      'b=',b,'\n'
      'b1=',b1)
i = np.arange(1,10,1)
j = np.arange(1,10,1).reshape(9,1)
table99 = np.array(j*i)
print(table99)
print(i)
print(j)
print(table99.size)
table99_1=np.array(table99).T
print(table99_1)
print(table99 == table99_1)
print(type(table99))

print(type(y))
table99_2 = np.array(table99).reshape(3,3,3,3)
print(table99_2)

table99_3 = table99.reshape(1,1,1,9,9)
print(table99_3)

#fig = plt.figure()
#plt.plot(i,j)
plt.plot(table99)
plt.title(u"中文显示ok")
plt.xlim()
plt.grid(ls="-.")




plt.show()

