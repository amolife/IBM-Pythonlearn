#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

n = int(input("input number:"))

a = n % 10
b = n // 10 % 10
c = n // 100 % 10

print(a, b, c)
