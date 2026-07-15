import numpy as np

#Create an array of 10 random integers between 1 and 100.
random_integers = np.random.randint(1, 101, size=10)
print(random_integers)

#Create an array of 5 random floating-point numbers between 0 and 1.
random_floats = np.random.rand(5)
print(random_floats)

#Find the minimum and maximum in a random array.
random_array = np.random.rand(10)
min_value = np.min(random_array)
max_value = np.max(random_array)
print(f"Random Array: {random_array}")
print(f"Minimum Value: {min_value}")
print(f"Maximum Value: {max_value}")

#Find the index of the largest value in an array.
random_array = np.random.rand(10)
index_of_max = np.argmax(random_array)
print(f"Random Array: {random_array}")
print(f"Index of Largest Value: {index_of_max}")


