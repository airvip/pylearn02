#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/5 22:41.

import random

"""
知识点：
1. import 初识
2. if ... elif ... else
3. 逻辑判断
3. 长判断代码格式调整
"""

# 剪刀石头布小游戏
you = int(input("请输入您的出拳【0.剪刀 1.石头 2.布】："))

# 计算机出拳
computer = random.randint(0, 2)

info = ["剪刀", "石头", "布"]

# 输出计算机与你的出拳
print("计算机的出拳为【{}】,你的出拳为【{}】.".format(info[computer-1], info[you-1]))

if ((you == 0 and computer == 2)
        or (you == 1 and computer == 0)
        or (you == 2 and computer == 1)):
    print("你赢了...")
elif you == computer:
    print("平局, 再来一次")
else:
    print("不愧是计算机")
