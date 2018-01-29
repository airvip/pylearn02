#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/1/29 23:53.

# 动态输入多少斤瓶子
weight_str = input("请输入多少斤瓶子:")
weight_float = float(weight_str)

# 每斤 输入每斤价格
price_str = input("请输入多少每斤瓶子的价格:")
price_float = float(price_str)

# 总共卖了 total 元
total_price = price_float * weight_float
print(total_price)

