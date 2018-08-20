#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/20 16:48.

def select_sort(nums):
    for i in range(len(nums) - 1):
        now_min = i
        for j in range(i+1, len(nums)):
            if nums[now_min] > nums[j]:
                now_min = j
        nums[i], nums[now_min] = nums[now_min], nums[i]
    return nums

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = select_sort(list_nums)
    print(list_res)