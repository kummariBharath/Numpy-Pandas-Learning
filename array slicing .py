import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[0:6]) #start:stop:step

#negative slice on 1-d array 
import numpy as np
arr=np.array([23,43,44,22,45])
print(arr[-5:-1]) #slice same array using the negative slice
print(arr[-5:-1:2]) #slice  the same array using the negative slice with step
print(arr[-3:-1])#Slice from the index 3 from the end to index 1 from the end 

#using the step argument on 1-d array
import numpy as np
arr1=np.array([1,2,3,4,5,6,78,9,20])
print(arr1[1:7:2])
print(arr1[::2])# Slice the array from the start to the end with step 2
print(arr1[::3])# Slice the array from the start to the end with step 3
print(arr1[-1:-10:-1])# Slice the array from the end to the start with step -1
print(arr1[-1:-10:-2])# Slice the array from the end to the start with step -2
print(arr1[::-1])#reverse the array using slicing
print(arr1[::-2])#reverse the array using slicing with step -2

#Slicing on 2-d array
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4]) #slice the second row from index 1 to index 4
print(arr[0:2, 2]) #slice the first two rows from index 2 where index 2 is the printing of the third column



