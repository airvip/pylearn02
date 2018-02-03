#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/4 0:05.

# if 基本语法

"""
if 要判断的条件:
    条件成立时要执行的代码
"""

age = int(input("请输入你的年龄："))
print(age, type(age))
if age >= 18:
    print("现在是成年人了...")

"""
if 要判断的条件:
    条件成立时要执行的代码
else:
    条件不成立时要执行的代码
"""
age = int(input("请输入你的年龄："))

if age >= 18:
    print("现在是成年人了...")
else:
    print("你还是不是成年人...")

"""
if 要判断的条件1:
    条件1成立时要执行的代码
elif 要判断的条件2:
    条件2成立时要执行的代码
else:
    条件都不成立时要执行的代码
"""

age = int(input("请输入你的年龄："))

if age >= 18:
    print("现在是成年人了...")
elif age >= 10:
    print("出于青春期了...")
else:
    print("童年快乐...")
