# Creating multiplication table

def multitable(mul1, mul2):
    for factor in range(1,mul2+1):
        print(f'{int(mul1)} * {int(factor)} = {int(mul1) * int(factor)}')

try:

    multi1 = input('Enter the multiplicand')
    multi2 = input('Enter the multiplier')

    if not multi1.isdigit():
        raise ValueError('Multiplicand is invalid type')

    if not multi2.isdigit():
        raise ValueError('Multiplier is invalid type')

    if ( int(multi1) <= 0 or int(multi2) <= 0):
        raise ValueError('Value cannot be either zero or negative')

    multitable(int(multi1), int(multi2))

except ValueError as ep:
    print(f'Invalid input: {ep}')


