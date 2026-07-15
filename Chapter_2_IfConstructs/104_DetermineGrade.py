# Input the score out of 100 and determine the corresponding grade
import sys

class ScoreError(Exception):
    """Exception raised for specific business logic errors."""
    pass

sMark = input('Enter the score out of 100\n')

try:
    nMark = int(sMark)
    if nMark < 0 or nMark > 100:
        raise ScoreError("The score has to be between 0 and 100")

    # determine the grade
    if nMark >=98 and nMark <= 100:
        Grade = 'A+'
    elif nMark >=95 and nMark <= 97:
        Grade = 'A'
    elif nMark >=92 and nMark <= 94:
        Grade = 'A-'
    elif nMark >=89 and nMark <= 91:
        Grade = 'B+'
    elif nMark >=86 and nMark <= 88:
        Grade = 'B'
    elif nMark >=83 and nMark <= 85:
        Grade = 'B-'
    elif nMark >=80 and nMark <= 82:
        Grade = 'C+'
    elif nMark >=77 and nMark <= 79:
        Grade = 'C'
    elif nMark >=74 and nMark <= 76:
        Grade = 'C-'
    elif nMark >=71 and nMark <= 73:
        Grade = 'D+'
    elif nMark >=68 and nMark <= 70:
        Grade = 'D'
    elif nMark >=65 and nMark <= 67:
        Grade = 'D-'
    else:
        Grade = 'F'

    print(f'Your Grade is {Grade}')

except ValueError:
    print('The score has to be a numeric value')
except ScoreError as se:
    print(f'Invalid score. {se}')
    sys.exit(1)
