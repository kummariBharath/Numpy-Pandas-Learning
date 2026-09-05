import numpy as np
arr=np.array([1,2,3,4,5]) #1-d
print(arr[0])

#2--d array indexing
import numpy as np
arr=np.array([[1,2,3,4,54],[83,74,95,59,15]])
print(arr[0,3]) # first index is "row" and second index is "column"(inside the square brackets)

#3-d array indexing
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#2 → 2 → 3
#↑    ↑    ↑
#│    │    └── elements(all innermost lists actually contained 3 elements)
#│    └─────── lists per group()
#└──────────── groups(dimension)
print(arr[0,1,1]) #the first index is dimension(from the outermost array), 
                  #the second index is inside the first array of the first dimension,
                  #the third index is inside the second array of the first dimension

#negative indexing
import numpy as np
arr=np.array([[1,2,3,4,54],[83,74,95,59,15]])
print(arr[-1,-1]) # prints the last element of the last row



