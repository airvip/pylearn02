#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/4 0:41.

age = int(input("请输入你的年龄："))
if age >= 0 and age <= 120:
    print("您的年龄是 {}".format(age))
else:
    print("不用猜了，你这智商也是有问题...")

if age < 0 or age > 120:
    print("不用猜了，你这智商也是有问题...")
else:
    print("您的年龄是 {}".format(age))
