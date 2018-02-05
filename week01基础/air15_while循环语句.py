#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/5 23:12.

"""
while 条件(判断 计数器 是否达到 目标次数):
    条件满足需执行的事情

    处理条件（技术器加一）
"""
# 输出 5 遍"我是帅哥"
print("我是帅哥")
print("我是帅哥")
print("我是帅哥")
print("我是帅哥")
print("我是帅哥")

print("分割线".center(20, "*"))

# 用 while 实现
i = 0
while i < 5:
    print("我是帅哥")
    # 一定要处理计数器
    i += 1
