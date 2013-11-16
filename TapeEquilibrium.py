# -*- coding: utf-8 -*-
"""
    A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non−empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:
P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7

The function should return '1' as answer
"""

import time
s=time.time()
def solution(a):
    y=len(a)
    if y<2:
        return False
    if y==2:
        return abs(a[1]-a[0])
    total=sum(a)
    left = a[0]
    minimum = abs(total - 2*left)
    for i in range(1,y):
        left+=a[i]
        temp = abs(2*left - total)
        if minimum > temp:
            minimum=temp
    return minimum            
print solution([3,1,2,4,3])
print time.time()-s
