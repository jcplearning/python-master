# filter words

def filter_words(*strings): 
    filtered = []
    for string in strings:
        if 'Python' in string:
            filtered.append(string)
    return filtered

def filter_words_comprehension(*strings): 
    return(list(string for string in strings if 'python' in string.lower()))

strings = ['Python is awesome','I love Java','Python is great','I dislike bugs']

print(filter_words(*strings))
print(filter_words_comprehension(*strings))  
