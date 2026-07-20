import sys
# convert celcius to fahrenheit and vice versa

scale = input('Enter "c" to input Celsius or "f" for fahrenheit')

if scale.upper() != 'C' and scale.upper() != 'F':
    print('Invalid scale selection. exiting...')
    sys.exit(1)

try:
    temp = input('enter the temperature')
    tempint = int(temp)

    if  scale.upper() == 'C' :
        convtemp = ( tempint * 9/5) + 32
        print(f'The corresponding temp in fahrenheit is {convtemp}')
    else:
        convtemp = ( tempint - 32 ) * 5/9
        print(f'The corresponding temp in celsius is {convtemp:.1f}')


except ValueError:
    print('Temperature is not numeric')

