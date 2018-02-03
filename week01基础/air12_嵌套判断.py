#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/4 0:58.

# 性别输入 ： 0 1 2
sex = int(input("请输入您想知道的性别代码【0,1,2】："))

if sex == 0:
    print("0 代表女性")
else:
    print("进入男性角色判断阶段")
    if sex == 1:
        print("1 代表纯爷们")
    else:
        print("2 代表你懂得")
