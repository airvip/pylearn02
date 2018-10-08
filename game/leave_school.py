#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

a = ['🙉', '🐉', '🐋', '🐕', '🐢', '🙌']

for i in range(len(a)):
# for i in range(0x1f600,0x1f650):
    for j in range(20):
        s = ' 学校' + ' ' * j + a[i]
        print(s+'\r', end='')
        time.sleep(0.05)


