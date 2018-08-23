#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2018/8/22 17:17.



def heap_sort(nums):
    def sift_down(start, end):
        root = start
        while True:
            # child 表示 root 节点的左孩子下标
            # end 表示最后一个节点的下标
            child = 2 * root + 1
            # child > end，说明 root 没有子节点
            if child > end:
                break
            # child + 1 < end 说明存在左孩子
            # child + 1 = end 说明存在右孩子
            if child + 1 <= end and nums[child] < nums[child + 1]:
                child += 1  # 右孩子大就用右孩子的下标做调整
            if nums[root] < nums[child]:  # 如果父节点小于孩子节点就交换
                nums[root], nums[child] = nums[child], nums[root]
                root = child  # 将子节点作为父节点进入下次循环判断是否有子节点
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