#!/usr/bin/env python

# encoding: utf-8

'''

@author: 谈超

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: itanchao@gmail.com

@software: PyCharm

@file: SelectSort.py

@time: 2017/4/19 上午11:29

@desc:

'''
def selectSort(array):
    '''
    每一次查找最小的一个数字转移到第一位 
    '''
    num = len(array)
    for i in range(0, num - 1):
        index = i
        print(array)
        for j in range(i + 1, num):
            print('%d----->%d' % (i, j))
            if array[index] > array[j]:
                index = j
        if index != i:
            tmp = array[i]
            array[i] = array[index]
            array[index] = tmp

    return array
# 对以下一组数据进行升序排序（选择排序）。“86, 37, 56, 29, 92, 73, 15, 63, 30, 8”
array = [24, 17, 85, 13, 9, 54, 76, 45, 5, 63]
selectSort(array)
print(array)