# Sum of n numbers
def n_sum(limit:int):
    return (limit * (limit +1 ))/2

def greet(name, message = 'Hello'):
    print(f'{message} {name}')

# Get the value(s) returned by the user defined function
sum_n = n_sum(10)
print(f'The sum is {sum_n}')

def pass_list(*frt):
    for fr in frt:
        print(fr)

# Pass the arguments using position or name or use the default
greet('Mr.Smith','Hi')
greet('Mr.Smith')
greet(message='Welcome', name = 'John')


# passing n number of arguments to a user defined function
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3))              # 6
print(total(10, 20, 30, 40, 50))   # 150
print(total())                     # 0

def sum_scores(**scores):
    total = 0
    for subject, score in scores.items():
        total += score
    return total

print(sum_scores(Math=85, Science=90, Literature=88))  # 263
