#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/30 15:00.

def count_sort(nums):
    leng = len(nums)
    res = [ None for i in range(leng)]
    for i in range(leng):
        if nums[i] in res:
            continue
        index_start = index_end = 0
        for j in range(leng):
            if nums[j] < nums[i]:
                index_start += 1  # 计算有多少个值小于 nums[i]
            elif nums[j] == nums[i]:
                index_end += 1  # 计算有多少个值等于 nums[i]
        for k in range(index_start, index_start + index_end):
            res[k] = nums[i]  # 确定 nums[i] 在 res 中的位置
    return res

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = count_sort(list_nums)
    print(list_res)