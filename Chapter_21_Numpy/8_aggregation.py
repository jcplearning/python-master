import numpy as np

#Compute the sum of all elements in a matrix.
matrix = np.array([[1, 2], [3, 4]])
sum_of_elements = np.sum(matrix)
#The function np.sum() calculates the sum of all elements in the given matrix. In this case, the sum is computed as follows:
#1 + 2 + 3 + 4 = 10
#After executing this code, the variable sum_of_elements will contain the sum of all elements in the matrix, which in this case will be 10.
print(sum_of_elements)
#Compute the cumulative sum of an array.
arr = np.array([1, 2, 3, 4, 5])
cumulative_sum = np.cumsum(arr)
#The function np.cumsum() computes the cumulative sum of the elements in the array arr.
#The cumulative sum is calculated by taking the sum of the elements up to each index in the array. In this case, the cumulative sum is computed as follows:
#Index 0: 1
#Index 1: 1 + 2 = 3
#Index 2: 1 + 2 + 3 = 6
#Index 3: 1 + 2 + 3 + 4 = 10
#Index 4: 1 + 2 + 3 + 4 + 5 = 15
#After executing this code, the resulting array cumulative_sum will contain the cumulative sums of the original elements, which in this case will be [1, 3, 6, 10, 15].
print(cumulative_sum)

#Compute row-wise sums.
matrix = np.array([[1, 2], [3, 4]])
row_wise_sums = np.sum(matrix, axis=1)
#The function np.sum() with the parameter axis=1 calculates the sum of elements along each row of the given matrix. In this case, the row-wise sums are computed as follows:
#Row 0: 1 + 2 = 3
#Row 1: 3 + 4 = 7
#After executing this code, the resulting array row_wise_sums will contain the sums of
#    each row in the matrix, which in this case will be [3, 7].
print(row_wise_sums)


#Compute column-wise means.
matrix = np.array([[1, 2], [3, 4]])
column_wise_means = np.sum(matrix, axis=0)
print(column_wise_means)

#Find the cumulative product of an array.
arr = np.array([1, 2, 3, 4, 5])
cumulative_product = np.cumprod(arr)
#The function np.cumprod() computes the cumulative product of the elements in the array arr.
#The cumulative product is calculated by taking the product of the elements up to each index in the
#array. In this case, the cumulative product is computed as follows:
#Index 0: 1
#Index 1: 1 * 2 = 2
#Index 2: 1 * 2 * 3 = 6
#Index 3: 1 * 2 * 3 * 4 = 24
#Index 4: 1 * 2 * 3 * 4 * 5 = 120
#After executing this code, the resulting array cumulative_product will contain the cumulative products of the original
#elements, which in this case will be [1, 2, 6, 24, 120].
print(cumulative_product)

#Count how many elements are nonzero.
arr = np.array([0, 1, 2, 0, 3, 0, 4])
nonzero_count = np.count_nonzero(arr)
#The function np.count_nonzero() counts the number of non-zero elements in the given array arr. In this case, the non-zero elements are 1, 2, 3, and 4. Therefore, the count of non-zero elements is 4. After executing this code, the variable nonzero_count will contain the count of non-zero elements in the array, which in this case will be 4.
print(nonzero_count)

#Find the median of an array.
arr = np.array([1, 2, 3, 4, 5])
median_value = np.median(arr)
#The function np.median() calculates the median of the elements in the array arr. The median is the middle value of a sorted list of numbers. In this case, the sorted array is [1, 2, 3, 4, 5], and the middle value is 3. After executing this code, the variable median_value will contain the median of the array, which in this case will be 3.0.
print(median_value)

#Find unique values in an array.
arr = np.array([1, 2, 2, 3, 4, 4, 5])
unique_values = np.unique(arr)
#The function np.unique() finds the unique values in the given array arr. In this case, the unique values are 1, 2, 3, 4, and 5. After executing this code, the resulting array unique_values will contain the unique values from the original array, which in this case will be [1, 2, 3, 4, 5].
print(unique_values)


