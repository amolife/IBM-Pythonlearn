#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:55:55 2019

@author: debianibm 
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

csv_list = []
with open("./datacsv2.csv", "rt", encoding="utf8") as file:
    lines = csv.reader(file)
    print(lines)
    for line in lines:
        csv_list.append(line)
#          print(line)
csv_list = np.array(csv_list, dtype=int)

fig, axes = plt.subplots(2, 1)
ax1 = axes[0]
ax2 = axes[1]

x = csv_list[:, 0]  # lines of row #0
y = csv_list[:, 1]  # lines of row #1
ax1.set_title("Title-ax1")
# ax1.set_xlim(0,100)
# ax1.set_ylim(0,100)
# ax1.set_xscale("linear")
ax1.scatter(x, y, marker="*", c="b", edgecolors="b")
# ax2.set_title("Title-ax2")
ax1.grid(axis='x')
ax2.plot(x, y, "b*")
plt.show()
