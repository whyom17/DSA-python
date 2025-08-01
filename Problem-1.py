# PROBLEM STATEMENT : Given an array X. Compute the array A such that A[i] is the average of elements X[0]. . . X[i], for i = 0....n − 1. 
# You can solve this with two methods, one with O(n^2) and one with O(n) time complexities. 
# Compare time complexities of both the methods by experimental approach plotting graph between ‘n’ and time taken for execution.

import numpy as np

X= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
A= np.zeros(len(X), dtype=float)


# method-1 : O(n)
def average_array(X):
    for i in range(len(X)):
        A[i] = np.mean(X[:i+1])
    return A
print ("Average array using O(n) method:", average_array(X))


# method-2 : O(n^2)
def sum_arr(arr):
    sum=0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def average_array(X):
    for i in range(len(X)):
        A[i] = sum_arr(X[:i+1])/len(X[:i+1])
    return A

print ("Average array using O(n) method:", average_array(X))