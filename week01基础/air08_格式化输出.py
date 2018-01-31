#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/1/31 23:37.

# %s 字符串
# %d 有符号十进制整数  %3d 表示输出的整数显示位数，不足的地方使用 0 补全
# %f 浮点数 %.02f 表示小数点后只显示两位
# %% 输出 %


print("收的瓶子每斤 %f 元" % 1.90)

price = 1.90
print("收的瓶子每斤 %.2f 元" % price)


print("%.2f 斤瓶子 %.2f 元" % (12.6, 1.90 * 12.6))

weight = 12.6
total_price = price * weight
print("%.2f 斤瓶子 %.2f 元" % (weight, total_price))
