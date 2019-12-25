#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:04:27 2019
@author: debianibm
"""

import requests
import sys
from lxml import etree
from requests import structures
import math
import os
import time
from collections import Iterable,Iterator
import builtins  # 可以查看内建函数
from PIL import Image 
import argparse  #构造命令

gheads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87,Safari/537.36", }

urltest = 'http://www.baidu.com'
urltest2 = urltest+'/robots.txt'
html = requests.get(urltest, headers=gheads)
content_byte = html.content  # byte
content_decode = content_byte.decode('utf-8')  # byte decode to UTF-8
text = html.text  # text


header = html.headers
header_ordered = structures.OrderedDict(
    html.headers)  # actually equal == header
# print(geturl.__dict__)


selector = etree.HTML(text)
#info = selector.xpath('//div[@class="image"]/ul/li/text()')


# =============================================================================append,sort,reverse等，这些是就地执行的。而且作为函数返回，是None
# In [204]: 
# 
# In [204]: l = [1,2,3]
# 
# In [205]: l.append(4)
# 
# In [206]: l
# Out[206]: [1, 2, 3, 4]
# 
# In [207]: l2 = l.append(5)
# 
# In [208]: l2
# 
# In [209]: l2
# 
# In [210]:  # l2 返回的是None
# =============================================================================

# ============================================================================= append, extend
# In [185]: l = [1,2,3]
# In [187]: l.append([4,5])
# In [188]: l
# Out[188]: [1, 2, 3, [4, 5]]
# In [189]: l.extend([6,7])
# In [190]: l
# Out[190]: [1, 2, 3, [4, 5], 6, 7]
# In [191]: l.extend(8,9)
# Traceback (most recent call last):
#   File "<ipython-input-191-ecb1d78f45c4>", line 1, in <module>
#     l.extend(8,9)
# TypeError: extend() takes exactly one argument (2 given)
# 
# =============================================================================
# =============================================================================generator 生成器，[] 换成 () 如果在函数中变成generator，就用yield + 某个
# In [169]: L = [x*2 for x in range(10)]
# In [170]: L
# Out[170]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 
# In [171]: G = (x*2 for x in range(10))
# In [172]: G
# Out[172]: <generator object <genexpr> at 0xabddb1ac>
# In [173]: next(G)
# Out[173]: 0
# In [174]: next(G)
# Out[174]: 2
# In [175]: next(G)
# Out[175]: 4
# In [176]: next(G)
# Out[176]: 6
# =============================================================================
# =============================================================================检查迭代对象，迭代器
# from collections import Iterable,Iterator
# In [157]: isinstance([],Iterator)
# Out[157]: False
# 
# In [158]: isinstance([],Iterable)
# Out[158]: True
# iter()可以把不是Iterator的对象变成iterator
# 凡是可作用与for循环的对象都是Iterable
# 凡是可作用于next()函数的对象都是Iterator =============================================================================

# =============================================================================try语句，注意else是和try结合的，不是和if
# In [125]: while True:
#      ...:     inp = input()
#      ...:     try:
#      ...:         inp is int(inp)
#      ...:     except:
#      ...:         raise ValueError
#      ...:     else:
#      ...:         print(int(inp)**2)
#      ...: print('bye')
#
# 2
# 4
#
# 5
# 25
#
# a
# Traceback (most recent call last):
#
#   File "<ipython-input-125-36b72c7fa54f>", line 6, in <module>
#     raise ValueError
#
# ValueError
# =============================================================================

# =============================================================================检查字符串是否为数字
# In [111]: '1'.isdigit()
# Out[111]: True
#
# In [112]: 'z'.isdigit()
# Out[112]: False
#
# In [113]: '0'.isdigit()
# Out[113]: True
#
# In [114]: '中'.isdigit()
# Out[114]: False
#
# =============================================================================

# =============================================================================计算函数运行时间 require import time
# In [91]: def timer(func,*pargs):  #运行1000遍
#     ...:     start = time.process_time()
#     ...:     for i in range(1000):
#     ...:         func(*pargs)
#     ...:     elapsed = time.process_time() - start
#     ...:     return (elapsed,func(*pargs))
#     ...:
#     ...:
#
# In [92]:  # 一个测试函数
# def test1():
#    for i in range(9999):
#        t = i ** 0.5
#    return i
#     ...:
#     ...:
#
# In [93]: test1() # test1 return i=9998
# Out[93]: 9998
#
# In [94]: timer(test1)  # 测试1000遍的 for 9999遍历
# Out[94]: (0.6788726489999988, 9998)  # 输出运行时间和函数返回的结果
# =============================================================================

# ==========================================================timer构造测用时===================
# In [31]: def timer():
#     ...:     start = time.process_time()
#     ...:     for i in range(1000):
#     ...:         res = math.sqrt(i**100)
#     ...:     elapse = time.process_time() - start
#     ...:     return 'time spend:',elapse
#     ...:
#     ...:
#
# In [32]: timer()
# Out[32]: ('time spend:', 0.006529758000000108)
#
# =============================================================================
# =============================================================================
#
# In [108]: lstemp = [1,]
# In [109]: print(lstemp)
# [1]
# In [111]: print(lstemp.append(2))
# None
# In [112]: print(lstemp)
# [1, 2]
# In [113]: print(lstemp.append(2))
# None
#
# =============================================================================

# %timeit %time 是ipython 的命令
# time 是bash的命令，time 是 shell 关键字;;;;;;;;脚本中可以写!time,比如vimrc中加的时间

#import time
# time
# Out[163]: <module 'time' (built-in)>
# time.clock
# Out[173]: <function time.clock>
# time.clock()
# __main__:1: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
#Out[172]: 21.856122
# =============================================================================
# def calsqrt(n):
#    for i in range(n):
#        res =  math.sqrt(i)
#        print(res)
#    return i,res
#
#
#
# calsqrt(10)
# 0.0
# 1.0
# 1.4142135623730951
# 1.7320508075688772
# 2.0
# 2.23606797749979
# 2.449489742783178
# 2.6457513110645907
# 2.8284271247461903
# 3.0
# Out[87]: (9, 3.0) # 返回给调用函数calsqrt()的人(return res）
# =============================================================================

# =============================================================================交换x,y
# In [67]: x=10
# In [68]: y=90
# In [69]: x,y=y,x
# In [70]: x
# Out[70]: 90
# In [71]: y
# Out[71]: 10
# =============================================================================

# =============================================================================
# In [40]: [x + y for x in 'ABC' for y in 'MNL']
# Out[40]: ['AM', 'AN', 'AL', 'BM', 'BN', 'BL', 'CM', 'CN', 'CL']
#
# =============================================================================
# =============================================================================
#
# for temp in open('./webspider.py'):
#     print(temp.upper(),end='')
# =============================================================================
#D = {'a':1,'b':2,'c':3}
# for key in D.keys():
#    print(key,D[key])

#L = [1,2,3]
#L = [x + 90 for x in L]
# L
# =============================================================================
# byte encode and decode

# =============================================================================数值类型
# bin(2)
# Out[112]: '0b10'
# oct(2)
# Out[113]: '0o2'
# hex(2)
# Out[114]: '0x2'
# ord('2')
# Out[117]: 50
# chr(50)
# Out[124]: '2'
#
# int(2.001)
# Out[127]: 2
# float(2)
# Out[128]: 2.0
# =============================================================================

# =============================================================================数值换算
#
# ord('5')
# Out[1]: 53
#
# ord('0')
# Out[2]: 48
#
# hex(53)
# Out[3]: '0x35'
#
# hex(48)
# Out[4]: '0x30'
#
# b'\x35\x30'.decode(encoding='utf-8')
# Out[5]: '50'
#
# u'50'.encode(encoding='utf-8')
# Out[7]: b'50'
#
# u'50'.encode(encoding='gb2312')
# Out[8]: b'50'
#
# b'50'.decode(encoding='utf-8')
# Out[9]: '50'

# b'\x35\x30'==b'50'
# Out[11]: True =============================================================================字符转换


# 0x11
#Out[83]: 17

# ord('中')
#Out[71]: 20013
#
# chr(20013)
#Out[72]: '中'
#
# hex(20013)
#Out[73]: '0x4e2d'

# len(u'中'.encode(encoding='utf-8'))
#Out[87]: 3
#
# len(b'\xe4\xb8\xad'.decode(encoding='utf-8'))
#Out[88]: 1

# u'中'.encode(encoding='utf-8')
# Out[25]: b'\xe4\xb8\xad'
# b'\xe4\xb8\xad'.decode(encoding='utf-8')
# Out[26]: '中'

# u'中'.encode(encoding='gb2312')
#Out[65]: b'\xd6\xd0'
# b'\xd6\xd0'.decode(encoding='gb2312')
#Out[66]: '中'

# u'abc'.encode(encoding='iso8859-1')
# Out[80]: b'abc'
# =============================================================================
