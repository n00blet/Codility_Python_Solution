"""
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
"""
"""
Generalized solution
    1.total=sum(a)
    2.for i in range(min(a)):
        x+=i
    3.for i in range(max(a)+1):
        y+=1
    4.return y-x-total

The above code returns missing number within any range,i.e it need not be first N natural numbers
Ex - (11,12,14)

Note:This works if and only if 1 number is missing 
"""
import time
s=time.time()
def solution(a):
    n=len(a)
    if max(a)>n+1:
        return -1
    if n==0:
        return 1
    sums=(n+2)*(n+1)/2
    for i in range(n):
        sums-=a[i]
    return sums
    
print solution([2])
print time.time()-s
    
    
