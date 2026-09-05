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
print(arr[0:2, 1:4]) #slice the first two rows from index 1 to index 4 where index 1 to index 4 is the printing of the second column to the fourth column
print(arr[-3:-1, -4:-1]) #slice the first two rows from index 1 to index 4 where index 1 to index 4 is the printing of the second column to the fourth column using negative slicing
print("ANS",arr[-2:,-4:-1:1])#starts from the second last row to the last row and slice from the second column to the fourth column with step 1


#slicing on 3-d array
import numpy as np 
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,1]) #prints the second element of the second array of the first array of the first dimension 
print(arr[0:2, 0:2, 1]) #prints the second element of the first two arrays of the first two arrays of the first dimension

#arr[dimension1, dimension2, dimension3] 
#arr[  groups , rows , columns ]
#arr = np.array([
#    [[1, 2, 3],       # Group 0
#     [4, 5, 6]],

#    [[7, 8, 9],       # Group 1
#     [10, 11, 12]]
#     ])
#   2 groups × 2 rows × 3 columns

import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[78,89,100],[100,111,112]]])
print("everything is printed",arr[:,:,:]) #everything is printed
print("First group Result",arr[0,:,:]) #First group Result:[[1, 2, 3],[4, 5, 6]]
print("Last group using negative index",arr[-1,:,:])#Last group using negative index
print("All groups, first row",arr[:,0,:])
print("All groups, all rows, first 2 columns",arr[:,:,:2])
print(arr[::-1])

#example1
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[::-1,:]) #reverse the row order
                   #result:[[ 6  7  8  9 10] [ 1  2  3  4  5]]
print(arr[::-1,::-1])#reverse row orderr and reverses the inner rows(columns)

#example 2
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr[::2,:,:]) #starts with outer group 0 with step 2 selects the group 1 and 2 ,while rows and columns remain same

#example 3
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[-1:-3:-1, -1:-3:-1])
#the row slice from back to first -1 to -3 ,selecting rows 2 and 1;the column slice similarly selecting the columns 2 and 1(0 is excluded)

#example 4
import numpy as np
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(arr[:,:,-3:-1]) # keeping the dimensions (group and row ) same ,only columns selects two (-3,-2)

#example 5
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr[-2:,-2:,-3:-1]) #the last two groups and their last two rows are selected ,while the columns are -3 and -2(inner-most array)

#example 6
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(arr[-1:-4:-2,::2])#Rows are selected from back (-1 to -4) with step -2 ,selecting rows 3 & 1 ,column with step 2(inner(inside) array)

#example 7
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("example 6",arr[0,::-1,:]) #selecting first dimesnion(group),then reversing rows in group 1 ,keeping the column same

#example 8
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("example 8",arr[0,:,::-1]) #selecting first dimesnion(group),then keeping the rows inside group same,reversing the columns(array(inner))





