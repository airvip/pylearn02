#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by Admin on 2018/2/14 22:57.

i = 1

while i <= 9:
    j = 1
    while j <= i:
        print("{} * {} = {}".format(j, i, i*j), end=' ')
        j += 1
    i += 1
    print()

