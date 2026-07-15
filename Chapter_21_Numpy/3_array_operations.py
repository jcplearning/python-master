import numpy as np

array1 = np.array([10,20,30])
array2 = np.array([0.3,0.45,0.6])

# Arithmetic operations on arrays
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)

#Compute the dot product of two vectors.
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)
#The dot product of two vectors is calculated by multiplying corresponding elements and summing the results.
#In this case, the dot product is computed as follows:
#(1 * 4) + (2 * 5) + (3 * 6) = 4 + 10 + 18 = 32
print(dot_product)

#Multiply a matrix by a vector.
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])
result = np.dot(matrix, vector)
#The multiplication of a matrix by a vector is performed by taking the dot product of each row
#of the matrix with the vector. In this case, the result is computed as follows:
#For the first row of the matrix: (1 * 5) + (2 * 6) = 5 + 12 = 17
#For the second row of the matrix: (3 * 5) + (4 * 6) = 15 + 24 = 39
#Thus, the resulting vector after multiplying the matrix by the vector is [17, 39].
print(result)

#Square every element in an array.
arr = np.array([1, 2, 3, 4, 5])
squared_arr = arr ** 2
#The expression arr ** 2 computes the square of each element in the array arr. This
#operation is performed element-wise, meaning that each element in the array is raised to the power of 2. After executing this code, the resulting array squared_arr will contain the squares of the original elements, which in this case will be [1, 4, 9, 16, 25].
print(squared_arr)

#Compute the square root of each element.
arr = np.array([1, 4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
#The function np.sqrt() computes the square root of each element in the array arr. This operation is performed element-wise, meaning that the square root is calculated for each individual element in the array. After executing this code, the resulting array sqrt_arr will contain the square roots of the original elements, which in this case will be [1.0, 2.0, 3.0, 4.0, 5.0].
print(sqrt_arr)

#Compute the mean of an array.
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
#The function np.mean() calculates the mean (average) of the elements in the array arr. It does this by summing all the elements in the array and then dividing by the number of elements. In this case, the mean is computed as follows:
#(1 + 2 + 3 + 4 + 5) / 5 = 15 / 5 = 3.0
#After executing this code, the variable mean_value will contain the mean of the array, which
#in this case will be 3.0.
print(mean_value)

#Compute the standard deviation of an array.
arr = np.array([1, 2, 3, 4, 5])
std_dev = np.std(arr)
#The function np.std() calculates the standard deviation of the elements in the array arr. The standard deviation is a measure of the amount of variation or dispersion in a set of values. It is computed using the following formula:
#std_dev = sqrt(mean((arr - mean(arr)) ** 2))
#In this case, the standard deviation is calculated as follows:
#1. Compute the mean of the array: mean(arr) = 3.0
#2. Subtract the mean from each element and square the result: (arr - mean(arr)) ** 2 = [4, 1, 0, 1, 4]
#3. Compute the mean of the squared differences: mean((arr - mean(arr)) ** 2) = (4 + 1 + 0 + 1 + 4) / 5 = 10 / 5 = 2.0
#4. Take the square root of the mean of the squared differences: std_dev = sqrt(2.0) ≈ 1.4142135623730951
#After executing this code, the variable std_dev will contain the standard deviation of the array,
#which in this case will be approximately 1.4142135623730951.
print(std_dev)

#Add 10 to every element in an array.
arr = np.array([1, 2, 3, 4, 5])
arr_plus_10 = arr + 10
#The expression arr + 10 adds the value 10 to each element in the array arr. This operation is performed element-wise, meaning that 10 is added to each individual element in the array. After executing this code, the resulting array arr_plus_10 will contain the original elements with 10 added to each of them, which in this case will be [11, 12, 13, 14, 15].
print(arr_plus_10)

