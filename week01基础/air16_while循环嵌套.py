#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/5 23:41.

"""
while 条件(判断 计数器 是否达到 目标次数):
    条件满足需执行的事情

    while 条件(判断 计数器 是否达到 目标次数):
        条件满足需执行的事情

        处理条件（技术器加一）

    处理条件（技术器加一）
"""

# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        if i < j:
            print()
            break
        else:
            # print("{} * {} = {}".format(i, j, i*j), end=" ")
            print("%d * %d = %2d" % (i, j, i*j), end=" ")
        j += 1
    i += 1

