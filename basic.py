

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