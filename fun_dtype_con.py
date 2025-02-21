import numpy as np
arr=np.array([1,23,2],dtype=np.int8)
arr2=np.float16(arr)
print(arr2.dtype)

# or

arr3=arr.astype(float)
print(arr3)
print(arr3.dtype)

