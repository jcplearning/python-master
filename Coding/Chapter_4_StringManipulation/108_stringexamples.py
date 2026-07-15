# 1. count of vowels in the string
mystring ='stability of data pipelines, comprehensive testing and deployment activities'

countofvowels=0

for char in mystring:
    if char.lower() == 'a' or \
        char.lower() == 'e' or \
        char.lower() == 'i' or \
        char.lower() == 'o' or \
        char.lower() == 'u':
        countofvowels+=1

print(f'The count of vowels in the word {mystring} is {countofvowels}')

# 2. "  Hello, World!  ", produce "hello-world"
mystring = '  Hello, World!  '
print(mystring.strip().lower().replace(',','-').replace(' ',''))

# 3. Convert "snake_case_text" to "camelCaseText" using split(), title(), and join()

mystring = 'snake_case_text'
mylist = mystring.split('_')
print(mylist)
mylist[0] ='camel'
print(mylist)
mylist[1] = mylist[1].title()
mylist[2] = mylist[2].title()
print( "".join(mylist))


# 4. more frequent character in a strin
def most_frequent(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Find the character with the highest count
    max_char = max(counts, key=counts.get)
    return max_char, counts[max_char]


text = "programming"
char, freq = most_frequent(text)
print(f"Most frequent character: '{char}' (appears {freq} times)")






