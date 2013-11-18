# -*- coding: utf-8 -*-
"""
You are given N counters, initially set to 0, and you have two possible operations on them:
increase(X) − counter X is increased by 1,
max_counter − all counters are set to the maximum value of any counter.
A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:
if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max_counter.
For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.
"""

import time
s=time.time()
def solution(n,a):
    counter=[0]*n    
    m=0
    minValue=0
    for i in a:
        if 1<=i<=n:
            counter[i-1]=max(counter[i-1],minValue)+1
            print counter
            if counter[i-1]>m:
                m=counter[i-1]
        else:
            minValue=m
    for i in range(n):
        counter[i]=max(counter[i],minValue)
    return counter

print solution(5,[3,4,4,6,1,4,4])
print time.time()-s
