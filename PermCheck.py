"""
    A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation.
The goal is to check whether array A is a permutation.
Write a function:
"""


def solution(a):
	y=len(a)
	if y==0:
		return 0
	z=max(a)
	if z>y:
		return 0
	else:
		for i in a:
			if a.count(i)>1:
				return 0
			else:
				return 1
