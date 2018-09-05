#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/9/5 15:45.

def cocktail_sort(nums):
    length = len(nums)
    for i in range(length // 2):
        # 将最大值排到队尾
        for j in range(i, length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
        # 将最小值排到队首
        for j in range(length - 2 - i, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j],nums[j - 1] = nums[j - 1],nums[j]
    return nums

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = cocktail_sort(list_nums)
    print(list_res)