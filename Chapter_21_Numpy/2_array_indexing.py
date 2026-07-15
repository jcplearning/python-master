import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#Extract a 2x2 subarray from a 4x4 matrix.
arr = np.array([[1, 2, 3, 4], \
                 [5, 6, 7, 8], \
                      [9, 10, 11, 12],\
                          [13, 14, 15, 16]])
subarr = arr[1:3, 1:3]
#The first index (1:3) selects the rows from index 1 to 2 (inclusive), and the second index (1:3) selects the columns from index 1 to 2 (inclusive). This results in a 2x2 subarray containing the elements [[6, 7], [10, 11]].
print(subarr)

#Replace all odd numbers in an array with -1
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr[arr % 2 == 1] = -1
#The expression arr % 2 == 1 creates a boolean mask that identifies all the odd numbers in the array. The assignment arr[arr % 2 == 1] = -1 replaces all the elements in the array that satisfy this condition (i.e., all odd numbers) with -1. After executing this code, the resulting array will have all odd numbers replaced with -1, while even numbers will remain unchanged.
print(arr)

#Find all elements greater than 5.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
greater_than_5 = arr[arr > 5]
#The expression arr > 5 creates a boolean mask that identifies all the elements in the array that are greater than 5. The assignment greater_than_5 = arr[arr > 5] uses this boolean mask to extract and store all the elements that satisfy the condition (i.e., all elements greater than 5) into the variable greater_than_5. After executing this code, the variable greater_than_5 will contain an array of all the elements from the original array that are greater than 5, which in this case will be [6, 7, 8, 9].
print(greater_than_5)

#Use boolean indexing to keep only positive values.
arr = np.array([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]])
positive_values = arr[arr > 0]
#The expression arr > 0 creates a boolean mask that identifies all the elements in the array
#that are greater than 0 (i.e., positive values). The assignment positive_values = arr[arr > 0] uses this boolean mask to extract and store all the positive values from the original array into the variable positive_values. After executing this code, the variable positive_values will contain an array of all the positive values from the original array, which in this case will be [2, 4, 6, 8].
print(positive_values)

#Set all negative values in an array to 0.
arr = np.array([[-1, 2, -3], [4, -5, 6], [-7, 8, -9]])
arr[arr < 0] = 0
#The expression arr < 0 creates a boolean mask that identifies all the elements in the array
#that are less than 0 (i.e., negative values). The assignment arr[arr < 0] = 0 uses this boolean mask to set all the negative values in the original array to 0. After executing this code, the resulting array will have all negative values replaced with 0, while non-negative values will remain unchanged. In this case, the resulting array will be [[0, 2, 0], [4, 0, 6], [0, 8, 0]].
print(arr)
