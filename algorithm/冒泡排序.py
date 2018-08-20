#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/20 15:15.


def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 控制冒泡排序进行次数
        for j in range(len(nums) - i -1):  # 控制每次比较的次数
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = bubble_sort(list_nums)
    print(list_res)


