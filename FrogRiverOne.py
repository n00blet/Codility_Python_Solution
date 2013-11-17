# -*- coding: utf-8 -*-
"""
A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X. Leaves fall from a tree onto the surface of the river.
You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in minutes.
The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X.
For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In minute 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

If the frog is never able to jump to the other side of the river, the function should return −1.
"""
import time
s=time.time()
def solution(x,a):
    lst=[0]*(x)
    pathElem,t=0,0
    while(pathElem<x and t<len(a)):
        newLeaf=a[t]-1
        print 'nw',newLeaf
        if newLeaf<x:
            lst[newLeaf]+=1
            print lst
        if lst[newLeaf]==1:
            pathElem+=1
        t+=1
    if pathElem<x:
        return -1
    return t-1
            

print solution(5,[1,3,1,4,2,3,5,4])
print time.time() -s
