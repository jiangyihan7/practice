# -*- coding: utf-8 -*-
'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

#普通做法
def Find(target, array):
    for i in range(len(array)):
        if target in array[i]:
            return True
    return False

#复杂度低，从右上角开始
def Find2(target,array):
    m=len(array)
    n=len(array[0])
    flag=False
    row=0
    col=n-1
    while row<m and col>=0:
        if array[row][col]==target:
            flag=True
            break
        if array[row][col]<target:
            row+=1
        else:
            col-=1
    return flag
