""" 
A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a position greater than or equal to Y.
The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.
"""

import time
s=time.time()
def solution(X,Y,D):
    d=Y-X
    steps=d/D
    rem = d%D
    print 'rem',rem
    if rem!=0:
        steps+=1
    return steps
        
    
    
print solution(10,115,30)
print s-time.time()
# you can check for any large number of x and y and D,cuz the above solution has O(n) time complexity

