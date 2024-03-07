
class Author:
    def __init__(self, name: str, pen: str):
        self.name = name
        self.pen_name = pen

class Book:
    def __init__(self, name: str, author: Author = None):

        self.pages = 0
        self.name = name
        self.author = author

a = Author("Stephen King", "Bob")

b = Book("Carrie")

if b.author != None:
    print(f"The book is called {b.name} and the author is {b.author.name}")