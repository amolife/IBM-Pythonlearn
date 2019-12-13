#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

import string
import sys

s = input('请输入一个字符串:\n')

letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' %
      (letters, space, digit, others))
