import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

# original array is not affected
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

# original array is affected
print(arr)
print(x)
