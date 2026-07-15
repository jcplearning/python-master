# print only odd numbers

class InputError(Exception):
    pass

lowerlimit = input('Enter the lower limit in interger')
upperlimit = input('Enter the lower limit in interger')

try:
    n_ll = int(lowerlimit)
    n_ul = int(upperlimit)

    if n_ll > n_ul:
        raise InputError('Lower limit cannot exceed upper limit')

    while n_ll <= n_ul:
        if n_ll % 2 != 0:
            print(f'Next Odd number is {n_ll}')
        n_ll+=1

except ValueError:
    print('Invalid number for either upper or lower limit')
except InputError as IE:
    print(f'Invalid input. {IE}')




