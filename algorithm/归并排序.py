#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/21 14:30.


def merge(left_li, right_li):
    result = []
    while left_li and right_li:
        # 为了保持稳定性，当遇到相等的数据，优先把左侧的数放进结果列表，因为 left_li 的数据比 right_li 的数据靠左
        if left_li[0] <= right_li[0]:
            result.append(left_li.pop(0))
        else:
            result.append(right_li.pop(0))
    # while 循环结束，意味着一个列表为空，所以直接将剩余的列表添加到结果列表后面
    result += left_li
    result += right_li
    return result

def merge_sort(nums):
    if 1 == len(nums):  # 不断递归自己直到把自己拆分成单个元素
        return nums

    mid = len(nums) // 2  # 获取中间拆分位置
    left = nums[:mid]  # 得到左串
    right = nums[mid:]  # 得到右串

    left_li = merge_sort(left)
    right_li = merge_sort(right)
    return merge(left_li, right_li)

if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = merge_sort(list_nums)
    print(list_res)