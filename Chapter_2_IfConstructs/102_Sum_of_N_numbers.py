15
# sum of n numbers

def n_sum(nlimit):
    return (nlimit * (nlimit + 1))/2

limit = input('Enter the limit in integer')
try:
   nlimit = int(limit)
   nsum = n_sum(nlimit)
   print(f'The sum of first {nlimit} numbers is {nsum}')

except ValueError:
        print('Invalid number entered')


