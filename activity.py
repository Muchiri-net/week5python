# ====== Activity 1: My Book Classes ======

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

    def read(self):
        print(f"Opening {self.title} and reading... 📖")


# eBook subclass
class EBook(Book):
    def __init__(self, title, author, pages, size_mb):
        super().__init__(title, author, pages)
        self.size_mb = size_mb

    def show_info(self):
        print(f"{self.title} by {self.author}, {self.pages} pages (File: {self.size_mb} MB)")

    def read(self):
        print(f"Reading {self.title} on my device... 💻")


# Create books
book1 = Book("Drunk", "Jackson Biko", 200)
ebook1 = EBook("Americanah", "Chimamanda Ngozi Adichie", 477, 6)

# Use them
book1.show_info()
book1.read()
print("---")
ebook1.show_info()
ebook1.read()
