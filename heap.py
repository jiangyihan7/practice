# -*- coding: utf-8 -*-

def adjustheap(arr,i,size):
    left=2*i
    right=2*i+1
    maxIndex=i
    if i<size//2:
        if left<=size and arr[left]>arr[maxIndex]:
            maxIndex=left
        if right<=size and arr[right]>arr[maxIndex]:
            maxIndex=right
        if maxIndex!=i:
            arr[i],arr[maxIndex]=arr[maxIndex],arr[i]
            adjustheap(arr,maxIndex,size)

def buildheap(a,size):
    for j in range(size//2-1,-1,-1):
        adjustheap(a,j,size)

a = [1, 6, 4, 0, 3, 8]
i = len(a) - 1
while i >= 0:
    a[0], a[i] = a[i], a[0]
    buildheap(a, i)
    i = i - 1
print(a)