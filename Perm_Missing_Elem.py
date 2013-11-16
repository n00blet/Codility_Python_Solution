"""
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
"""

import time
s=time.time()
def solution(a):
    if len(a)<1:
        return False
    if len(a)==max(a):
        return False
    y=max(a)
    z=sum(a)
    c=y*(y+1)/2
    if z==c:
        return False
    return c-z    
    
print solution([2,1,3,5,4])
print time.time()-s
    
    
