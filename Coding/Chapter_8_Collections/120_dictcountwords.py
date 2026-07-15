paragraph = "Hello world! Hello everyone. Welcome to the world of Python programming. Python is great for data analysis. Python is also great for web development."

paragraph = paragraph.lower()
paragraph = paragraph.replace("!", "")
paragraph = paragraph.replace(".", "")

words = paragraph.split()
words_new = dict.fromkeys(words,0)
print(words_new)

for word in words:
    words_new[word] +=1

for word, count in words_new.items():
    print(f"{word}: {count}")

print(f'The most frequent word is "{max(words_new, key=words_new.get)}" with {max(words_new.values())} occurrences.')

