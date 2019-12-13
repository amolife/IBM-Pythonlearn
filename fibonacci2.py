#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

print("output 50 fibs:")
fibs = [1, 1]
for i in range(50):
    fibs.append(fibs[i]+fibs[i+1])
print(fibs)
