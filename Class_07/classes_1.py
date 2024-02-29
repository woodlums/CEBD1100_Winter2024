def sayhello():
    return "HEllo"

class Book:
    isbn = ""
    title = ""
    pages = 0

    def give_title(self):
        return self.title

    def get_minutes_to_read(self, level):

        if level == "expert":
            return self.pages * 5
        if level == "beginner":
            return self.pages * 10

book1 = Book() # Creating an instance called "book1".

book1.isbn = "123456789"
book1.pages = 330
book1.title = "Neuromancer"

print(book1)
print(book1.title)
print(book1.get_minutes_to_read("beginner"))
