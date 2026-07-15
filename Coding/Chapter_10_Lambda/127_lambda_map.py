celsius = [0, 10, 20, 30, 40]

fahrenheit = list(zip(celsius, map(lambda c: (c * 9/5) + 32, celsius)))
print(fahrenheit)

lst = [1, 2, 3, 4, 5]
squared = list(zip(lst,map(lambda x : x * x ,lst)))
print(squared)

strings = ["hello", "world", "python", "lambda"]

upper_strings = zip(strings,map(lambda string: string.upper(), strings)) 
print(list(upper_strings))





