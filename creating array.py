
#ndarray is array object in numpy
#when a list,tuple or any sequence is passed to the array() function, it is converted into an ndarray object.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array((2,3,4,4,4,4))
print(arr)
print(arr1)
print(type(arr))
print(type(arr1))
#checking the version of numpy
print(np.__version__)

###Dimensions of array##

#0-D each value in the array is a 0-D array
import numpy as np
arr=np.array(44)
print(arr)


#1-D array is an array that has 0-D arrays as its elements
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

#2-D array is an array that has 1-D arrays as its elements
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)

#3-D array is an array that has 2-D arrays as its elements
import numpy as np
arr1=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr1)

#4-D array is an array that has 3-D arrays as its elements
import numpy as np
arr2=np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],[[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]])
print(arr2)

#ndim is an attribute that returns an integer that tells us how many dimensions the array have.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr2=np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],[[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]])
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)