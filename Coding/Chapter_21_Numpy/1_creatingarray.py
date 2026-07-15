import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("Concatenate 1D:")
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("Concatenate 2D along axis 1:")
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print("Stack 1D along axis 1:")
print(arr)


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print("Horizontal stack 1D:")
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print("Vertical stack 1D:")
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print("Depth stack 1D:")
print(arr)


# Array split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("Split 1D into 3 parts:")
print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 2)
print("Split 2D into 2 parts:")
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("Indices where arr == 4:")
print(x)

arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr%2 == 1)
print("Indices where arr is odd:")
print(x)

# Sort
arr = np.array(['banana', 'cherry', 'apple'])
print("Sorted array:")
print(np.sort(arr))
    


# Array filter

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)


newarr = arr[filter_arr]

print("Original array:")
print(filter_arr)
print("Filtered array (only even numbers):")
print(newarr)

arr1 = np.square(newarr)
print("Square of the filtered array:")
print(arr1)

