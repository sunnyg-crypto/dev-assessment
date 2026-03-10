class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


# Create Book objects
book1 = Book(
    "Harry Potter and the Philosopher's Stone",
    "J.K. Rowling",
    "9780747532699",
    1997
)

book2 = Book(
    "The Alchemist",
    "Paulo Coelho",
    "9780061122415",
    1988
)

book3 = Book(
    "A Man Called Ove",
    "Fredrik Backman",
    "9781476738024",
    2012
)

# Print details
books = [book1, book2, book3]

for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Age:", book.get_age())
    print("Summary:", book.get_summary())
    print("-----------------------------")