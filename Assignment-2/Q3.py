from datetime import datetime

# Sample book data with borrow counts
library_books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "checked_out": False, "due_date": None, "borrow_count": 5},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "checked_out": True, "due_date": "2024-08-20", "borrow_count": 10},
    {"title": "1984", "author": "George Orwell", "checked_out": True, "due_date": "2024-08-10", "borrow_count": 7},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "checked_out": False, "due_date": None, "borrow_count": 4},
    {"title": "Moby Dick", "author": "Herman Melville", "checked_out": True, "due_date": "2024-08-15", "borrow_count": 8},
]

# Function to calculate the number of available books
def calculate_available_books(library_books):
    return len([book for book in library_books if not book["checked_out"]])

# Function to calculate the number of overdue books
def calculate_overdue_books(library_books):
    today = datetime.now().date()
    overdue_books = []
    for book in library_books:
        if book["checked_out"] and book["due_date"]:
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due_date < today:
                overdue_books.append(book)
    return overdue_books

# Function to determine the most borrowed book
def calculate_most_borrowed_book(library_books):
    most_borrowed_book = max(library_books, key=lambda book: book["borrow_count"])
    return most_borrowed_book

# Display insights
print("Library Insights:")
print(f"Total books available: {calculate_available_books(library_books)}")

overdue_books = calculate_overdue_books(library_books)
print(f"Total overdue books: {len(overdue_books)}")
if overdue_books:
    print("Overdue Books:")
    for book in overdue_books:
        print(f"  - {book['title']} by {book['author']} (Due: {book['due_date']})")

most_borrowed_book = calculate_most_borrowed_book(library_books)
print(f"Most borrowed book: {most_borrowed_book['title']} by {most_borrowed_book['author']} (Borrowed {most_borrowed_book['borrow_count']} times)")

# List books that are currently checked out
print("\nBooks Currently Checked Out:")
for book in library_books:
    if book["checked_out"]:
        print(f"  - {book['title']} by {book['author']} (Due: {book['due_date']})")
