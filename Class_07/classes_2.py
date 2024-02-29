def is_valid_isbn2(isbn):
    return True

class Book:

    def __init__(self, isbn, title, pages):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.price = 0.00

    def is_valid_isbn(self, isbn):
        # validate here.
        return True

    def get_minutes_to_read(self, level):

        if level == "expert":
            return self.pages * 5
        if level == "beginner":
            return self.pages * 10

book1 = Book("123456789", "Neuromancer", 330) # Creating an instance called "book1".

print(book1)
print(book1.title)
print(book1.get_minutes_to_read("beginner"))
