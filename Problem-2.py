# PROBLME STATEMENT: Write a program to sort an array (make a dynamic array) using Bubble sort. 
# Use 1-bit variable FLAG to signal when no interchange take place during pass. 
# If FLAG is 0 after any pass, then list is already sorted and there is no need to continue.

import time

def bubble_sort(A):
    for i in range(len(A),0,-1):
        FLAG=0
        for j in range(0,i-1):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                FLAG=1  # if swapped
                if not FLAG:
                    break
    
    print(A)
    end= time.time()
    print("Time taken to complete the process (in sec): ", end-start)
        
start= time.time()
        
bubble_sort([4,5,7,1,8])          