#Create a class Book with attributes title, author, and pages.
#Instantiate several Book objects and store them in a list.
#Loop through the list and print each book's title.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)
books = [book1, book2, book3]
for book in books:
    print(book.title)


             
