import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)

# create array with the specified datatype
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# change type
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
