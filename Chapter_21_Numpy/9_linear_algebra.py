import numpy as np

#Transpose a matrix.
matrix = np.array([[1, 2], [3, 4]])
transposed_matrix = np.transpose(matrix)
#The function np.transpose() takes the input matrix and returns its transpose. In this case, the original matrix is:
#[[1, 2],
# [3, 4]]
#The transposed matrix is obtained by swapping the rows and columns, resulting in:
#[[1, 3],
# [2, 4]]
print(transposed_matrix)

#Compute the inverse of a matrix.
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
#The function np.linalg.inv() computes the inverse of the given square matrix. In this case, the inverse of the matrix is:
#[[-2.   1. ]
# [ 1.5 -0.5]]
print(inverse_matrix)

#Solve a system of linear equations.
coefficients = np.array([[2, 1], [1, 3]])
constants = np.array([8, 13])
solution = np.linalg.solve(coefficients, constants)
#The function np.linalg.solve() solves the system of linear equations represented by the matrix equation Ax = b,
#where A is the coefficients matrix and b is the constants vector. In this case, the system of equations is:
#2x + y = 8
#x + 3y = 13
#The solution is x = 3, y = 5
print(solution)
