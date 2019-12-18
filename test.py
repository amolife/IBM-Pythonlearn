#d = {"m": 1, "n": 2, "b": 3}
# print(d["m"])
#
#a = 100
# print(hex(a))
# print(float('12.25'))


# def fx(n):
#   if n > 0:
#        pass
#   if n < 10:
#        pass
#   else:
#        return '不在0-10之間'
#
#
#a = fx(100)
# print(a)

#################################
#import math
#
# def move(x, y, step, angle):
#    newx = x+math.cos(angle)*step
#    newy = y+math.sin(angle)*step
#    return newx, newy
#
#
#c = move(0, 0, 100, math.pi)
# print(type(c))
# print(c[:])
# print(c)
#########################

# def fx(x, n):
#    xn = 1
#    while n > 0:
#        xn = xn*x
#        n = n-1
#    return xn
# print(fx(5,10000))

l = "abcdefghijklmnopqrstuvwxyz"
print(l[::5])
print(l[-1000::2])

print(l[-1000:1000:2])
print(l[0:1000:2])

a = "a".encode('utf-8')
print(ord(a))
b = '\u4e2d'
print(b)
