#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

rev = (1000000,600000,400000,200000,100000,0)
rate = (0.01,0.015,0.03,0.05,0.075,0.1)
revenue = float(input("income:"))
bonus = 0.0

for i in range(len(rev)):
    if revenue>rev[i]:
        bonus = bonus + rate[i]*(revenue - rev[i])
        #revenue = rev[i]
        #print(range(len(rev)))
        print(rate[i]*(revenue - rev[i]))
        revenue = rev[i]
  
print(bonus)

