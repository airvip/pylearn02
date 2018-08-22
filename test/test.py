#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/20 20:01.

# print(list(range(0,-1,-1)))
# print(list(range(1,-1,-1)))

l = len( [32, 24, 19, 55, 30, 22, 8]) // 2
print(l)
li_l = [32, 24, 19, 55, 30, 22, 8][:l]
print(li_l)
li_r = [32, 24, 19, 55, 30, 22, 8][l:]
print(li_r)

l_sort = []
l_sort.append(1)
print(l_sort)