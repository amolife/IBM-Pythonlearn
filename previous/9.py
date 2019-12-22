#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

import sys
import matplotlib
import time
if __name__ == "__main__":
    for i in range(11):
        print(10-i)
        time.sleep(1)
    print("Boo Boo")
    time.sleep(3)
    print(time.localtime(time.time()))
