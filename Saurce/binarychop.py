#!/usr/bin/env python

# encoding: utf-8

'''

@author: 谈超

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: itanchao@gmail.com

@software: PyCharm

@file: binarychop.py

@time: 2017/4/20 上午10:15

@desc:

'''
def binSort(array, goalNum , lowerlimit, toplimit):
    '''
    思想：每一次取中间元素去和目标值进行比较，确定上下限
    :param array: 数组
    :param goalNum: 目标元素
    :param lowerlimit: 下限
    :param toplimit: 上限
    :return: 目标元素的下标
    '''
    if lowerlimit < toplimit:
        mid = int((toplimit + lowerlimit)/2)
        if goalNum == array[mid]:
            return mid + 1
        else:
            return binSort(array,goalNum,mid+1,toplimit) if (goalNum > array[mid]) else binSort(array,goalNum,lowerlimit,mid-1)

array = [1,2,3,4,5,6,7,9,20,99,108,120,369,598]
index = binSort(array,goalNum= 108, lowerlimit = 0, toplimit= len(array)-1)
print(index)