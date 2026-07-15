import pandas as pd
import random

# Example for series from pandas module

mylist = ['Brazil','Argentina','Columbia','France','Germany','UK', 'USA']

se = pd.Series(mylist)

print('Shape:')
print(se.shape)

print('Array:')
print(se.array)

print('Values:')
print(se.values)

print('Dtype:')
print(se.dtype)

print('Describe:')
print(se.describe())

mynumlist = [random.randint(1,100), random.randint(1,100), random.randint(1,100) , random.randint(1,100)]

se = pd.Series(mynumlist)

print('Shape:')
print(se.shape)

print('Array:')
print(se.array)

print('Values:')
print(se.values)

print('Dtype:')
print(se.dtype)

print('Describe:')
print(se.describe())
