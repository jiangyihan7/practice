# -*- coding: utf-8 -*-
def merge(left,right):
    m=len(left)
    n=len(right)
    i, j = 0, 0
    a = []
    while i<m and j<n:
        if left[i]>=right[j]:
            a.append(left[i])
            i+=1
        else:
            a.append(right[j])
            j+=1
    if i==m:
        for i in range(j,n):
            a.append(right[i])
    else:
        for i in range(i,m):
            a.append(left[i])
    return a

a= [1,6,4,0,3,8]
def paixu(arr):
    if len(arr)<=1:
        return arr
    left=paixu(arr[0:len(arr)//2])
    right=paixu(arr[len(arr)//2:])
    return merge(left,right)
print(paixu(a))