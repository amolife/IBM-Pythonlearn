from matplotlib import pyplot as plt123

# 先生成画布
fig = plt123.figure()

# 然后正常画图

x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt123.bar(x, y, align =  'center')
plt123.bar(x2, y2, color =  'g', align =  'center')
plt123.title('Bar graph')
plt123.ylabel('Y axis')
plt123.xlabel('X axis')
plt123.show()


# 保存到文件
fig.savefig("test.png")  # 保存为png