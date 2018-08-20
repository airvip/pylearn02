#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/20 19:51.

def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]  # 当前需要排序的元素
        for j in range(i, -1, -1):
            if nums[j-1] > tmp:  # nums[j-1] 表示已有序的元素
                nums[j] = nums[j-1]
            else:
                break
        nums[j] = tmp
    return nums



# def insert_sort(nums):
#     for i in range(1, len(nums)):
#         tmp = nums[i]  # 当前需要排序的元素
#         j = i
#         while j :
#             if nums[j-1] > tmp:  # nums[j-1] 表示已有序的元素
#                 nums[j] = nums[j-1]
#             else:
#                 break
#             j -= 1
#         nums[j] = tmp
#     return nums

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = insert_sort(list_nums)
    print(list_res)



