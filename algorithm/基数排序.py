#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/31 17:31.

import math

def radix_sort(nums, radix=10):
    print(math.log(max(nums), radix))
    print(math.ceil(math.log(max(nums), radix)))
    K = int(math.ceil(math.log(max(nums), radix)))
    bucket = [[] for i in range(radix)]
    print(bucket)
    for i in range(1, K + 1):  # K次循环
        for val in nums:
            bucket[int(val % (radix ** i) / (radix ** (i - 1)))].append(val)  # 析取整数第K位数字 （从低到高）
        print(bucket)
        del nums[:]
        for each in bucket:
            nums.extend(each)  # 桶合并
        bucket = [[] for i in range(radix)]
    return nums


if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = radix_sort(list_nums)
    print(list_res)