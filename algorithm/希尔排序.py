#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/9/5 18:14.



def shell_sort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):
            while i >= step and nums[i - step] > nums[i]:
                nums[i], nums[i - step] = nums[i - step], nums[i]
                i -= step
        step = step // 2
    return nums




if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = shell_sort(list_nums)
    print(list_res)