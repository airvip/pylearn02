#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/23 17:26.

def quick_sort(nums, start, end):
    i = start
    j = end
    if i < j:
        base = nums[i]  # 设置基准，默认第一个值
        while i < j:
            # 从列表后面向前比较,如果数值比基准数大或相等,则前移一位直到有比基准数小的数出现
            while i < j and nums[j] >= base:
                j -= 1
            # 如果出现数值比基数小,则把第 j 个元素赋值给第 i 个元素,此时表中第 i,j 个元素相等
            nums[i] = nums[j]
            # 从列表前面向后比较,如果数值比基准数小或相等,则后移一位直到有比基准数大的数出现
            while i < j and nums[i] <= base:
                i += 1
            # 如果出现数值比基数大，则把第 i 个元素赋值给第 j 个元素,此时表中第 i,j 个元素相等
            nums[j] = nums[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        nums[i] = base
        quick_sort(nums, start, i - 1)
        quick_sort(nums, j + 1, end)
    return nums


if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = quick_sort(list_nums, 0, len(list_nums) - 1)
    print(list_res)