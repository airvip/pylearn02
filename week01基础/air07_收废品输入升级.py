#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/1/29 23:53.

# 动态输入多少斤瓶子
weight = float(input("请输入多少斤瓶子:"))

# 每斤 输入每斤价格
price = float(input("请输入多少每斤瓶子的价格:"))

# 总共卖了 total 元
total_price = price * weight
print(total_price)

