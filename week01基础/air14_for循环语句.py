#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/5 23:10.

"""
for 变量 in 序列:
    条件满足需执行的事情
else:
    条件不满足需执行的事情
"""

# range(101) == range(0, 101) 留头去尾
# 0 - 100 累加
sum100 = 0
for i in range(101):
    sum100 += i
else:
    print("循环结束, 0 - 100 累加结果:{}".format(sum100))

# 0 - 100 偶数累加
sum100 = 0
for i in range(101):
    if i % 2 == 0:
        sum100 += i
else:
    print("循环结束, 0 - 100 偶数累加结果:{}".format(sum100))

# 0 - 100 奇数累加
sum100 = 0
for i in range(101):
    if i % 2 != 0:
        sum100 += i
else:
    print("循环结束, 0 - 100 奇数累加结果:{}".format(sum100))

# 跳过 50 的 1-100 累加
sum100 = 0
for i in range(101):
    if i == 50:
        continue
    sum100 += i
else:
    print("循环结束, 跳过 50 的 1-100 累加结果:{}".format(sum100))

# 只累加到 50 的 1 - 100 累加
sum100 = 0
for i in range(101):
    sum100 += i
    if i == 50:
        break

print("循环结束, 只累加到 50 的 1 - 100 累加结果:{}".format(sum100))
