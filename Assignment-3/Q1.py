class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Initially, the book is available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"\n{self.name} has borrowed '{book.title}'")
        else:
            print(f"\nSorry, '{book.title}' is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"\n{self.name} has returned '{book.title}'")
        else:
            print(f"\n{self.name} has not borrowed '{book.title}'")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"\n{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(book)
        else:
            print(f"\n{self.name} has not borrowed any books")

    def __str__(self):
        return f"Member Name: {self.name}, Membership ID: {self.membership_id}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add new books to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"\nBook '{book.title}' added to the library.")

    # Register new members
    def register_member(self, member):
        self.members.append(member)
        print(f"\nMember '{member.name}' registered successfully.")

    # List all available books
    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("\nAvailable books in the library:")
            for book in available_books:
                print(book)
        else:
            print("\nNo books are currently available.")

    # List all borrowed books by a member
    def list_borrowed_books_by_member(self, member):
        member.list_borrowed_books()

# Create library object
library = Library()

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")

# Add books to library
library.add_book(book1)
library.add_book(book2)

# Create member
member1 = Member("Chetan", "C007")

# Register member
library.register_member(member1)

# List available books
library.list_available_books()

# Borrow a book
member1.borrow_book(book1)

# List available books after borrowing
library.list_available_books()

# List borrowed books by member
library.list_borrowed_books_by_member(member1)

# Return a book
member1.return_book(book1)

# List available books after returning
library.list_available_books()