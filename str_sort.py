# -*- coding: utf-8 -*-
'''
求任意一个字符串的全排列组合，例如a='123',输出 123，132，213，231，312，321。
'''
def str_sort(a):
    if a=='' or len(a)==1:
        return a
    else:
        s=[]
        for i in range(len(a)):
            for j in str_sort(a[0:i]+a[i+1:]):
                if (a[i]+j) in s:    #有重复时，判断结果中是否已有该字符串
                    continue
                else:
                    s.append(a[i]+j)
    return s

a='1233'
print(str_sort(a))
