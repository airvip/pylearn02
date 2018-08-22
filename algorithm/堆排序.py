#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/22 17:17.



def heap_sort(nums):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child + 1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(nums) - 2) // 2, -1, -1):
        sift_down(start, len(nums) - 1)

    # 堆排序
    for end in range(len(nums) - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end - 1)

    return nums


if __name__ == "__main__":
    list_nums = [32, 24, 19, 55, 30, 22, 8]
    list_res = heap_sort(list_nums)
    print(list_res)