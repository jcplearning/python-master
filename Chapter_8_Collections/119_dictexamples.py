#given a paragraph, return the most frequent word (case-insensitive, ignore punctuation)

import string
paragraph = "Hello world! Hello everyone. Welcome to the world of Python programming. Python is great for data analysis. Python is also great for web development."
# Remove punctuation and convert to lowercase
translator = str.maketrans('', '', string.punctuation)
print(type(translator))
print(translator)

cleaned_paragraph = paragraph.translate(translator).lower()
print(type(cleaned_paragraph))
print(cleaned_paragraph)

# Split the paragraph into words
words = cleaned_paragraph.split()
# Count the frequency of each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the most frequent word
most_frequent_word = max(word_count, key=word_count.get)
print(f"The most frequent word is '{most_frequent_word}' with {word_count[most_frequent_word]} occurrences.")

