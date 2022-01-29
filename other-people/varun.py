"""
Infosys exam for varun 28-Jan-2021
"""




""" 
Q2

You are given an array A containing N integers. You can do the following operations any number of times on the array

- choose any subarray of size K
- replace all the elements of that subarry with the maximum element of the chosen subarry

Find the minimum # of operations to make all the array elemetns equal.
"""

def answer(A, k):
    m = max(A)
    for i in range(len(A)):
        

A = [8,6,6,10,5]
k = 4              # ans 3

A = [1,2,3,4,5,5,5]
k = 3              # ans 2

A = [1,2,3,5,4,5,5]
k = 7              # ans 1