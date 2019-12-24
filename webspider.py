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

gheads = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87,Safari/537.36",}

urltest = 'http://www.baidu.com'
urltest2 = urltest+'/robots.txt'
html = requests.get(urltest,headers = gheads)
content_byte = html.content  # byte
content_decode = content_byte.decode('utf-8')  # byte decode to UTF-8 
text = html.text  # text



header = html.headers
header_ordered = structures.OrderedDict(html.headers)  # actually equal == header
#print(geturl.__dict__)

selector = etree.HTML(text)
#info = selector.xpath('//div[@class="image"]/ul/li/text()')

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
#for key in D.keys():
#    print(key,D[key])

#L = [1,2,3]
#L = [x + 90 for x in L]
#L
# =============================================================================
# byte encode and decode

# =============================================================================
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

# =============================================================================
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
#Out[11]: True =============================================================================


#0x11
#Out[83]: 17

#ord('中')
#Out[71]: 20013
#
#chr(20013)
#Out[72]: '中'
#
#hex(20013)
#Out[73]: '0x4e2d'

#len(u'中'.encode(encoding='utf-8'))
#Out[87]: 3
#
#len(b'\xe4\xb8\xad'.decode(encoding='utf-8'))
#Out[88]: 1

# u'中'.encode(encoding='utf-8')
# Out[25]: b'\xe4\xb8\xad'
# b'\xe4\xb8\xad'.decode(encoding='utf-8')
# Out[26]: '中'

# u'中'.encode(encoding='gb2312')
#Out[65]: b'\xd6\xd0'
#b'\xd6\xd0'.decode(encoding='gb2312')
#Out[66]: '中'

#u'abc'.encode(encoding='iso8859-1')
#Out[80]: b'abc'
#=============================================================================