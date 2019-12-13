#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

import sys
import time


def bar():
    i = 0
    while i < 100:
        i += 1
        time.sleep(1)
        sys.stdout.write(str(i) + '\r')


bar()
