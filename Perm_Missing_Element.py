"""
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
"""

import time
s=time.time()
def solution(a):
    c=len(a)
    if c==0:
        return 1
    if c==1 and a[0]==2:
        return 1
    if c==1 and a[0]>2:
        return -1
    if c==max(a):
        return -1
    x,y=0,0
    for i in range(1,min(a)):
        x+=i
    for i in range(1,max(a)+1):
        y+=i
    return y-x-sum(a)
    
print solution([2])
print time.time()-s
    
    
