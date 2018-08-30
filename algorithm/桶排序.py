#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/30 18:09.

def bucket_sort(nums):
    max_num = max(nums)
    bucket = [ 0 ] * (max_num + 1)
    print(max_num + 1)
    for i in nums:
        bucket[i] += 1

    res = []
    for i, v in enumerate(bucket):
        if v != 0:
            for v in range(v):
                res.append(i)

    return res


if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = bucket_sort(list_nums)
    print(list_res)