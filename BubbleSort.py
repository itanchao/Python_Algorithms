#!/usr/bin/env python

# encoding: utf-8

'''

@author: 谈超

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: itanchao@gmail.com

@software: PyCharm

@file: BubbleSort.py

@time: 2017/4/19 上午10:33

@desc:

'''

#  对以下一组数据进行降序排序（冒泡排序）。“24，17，85，13，9，54，76，45，5，63”
def bubbleSort(array):
    num = len(array)
    for i in range(0, num):
        for j in range(0, (num - i - 1)):
            if array[j] < array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array

array = [24, 17, 85, 13, 9, 54, 76, 45, 5, 63]
list1 = bubbleSort(array)
print(list1)
