#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_


def fib(n):
    if n <= 0:
        return print("Pls input nubmers>0")
    if n == 1:
        fibs = [1]
        return print(fibs)
    if n == 2:
        fibs = [1, 1]
        return print(fibs)
    else:
        fibs = [1, 1]
        for i in range(2, n):
            fibs.append(fibs[-1]+fibs[-2])
        return print(fibs)


N = int(input("how many nums?:"))
fib(N)
