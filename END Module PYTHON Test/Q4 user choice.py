import pickle
import re
import os

class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def __str__(self):
        return f"ID: {self.book_id}, Name: {self.name}, Author: {self.author}, Price: {self.price}"

class BookStore:
    def __init__(self, filename="books.dat"):
        self.filename = filename
        self.books = self.load_data()

    # Load data from pickle file
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return []

    # Save data to pickle file
    def save_data(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.books, f)

    # Add new book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        price = input("Enter Book Price: ")
        self.books.append(Book(book_id, name, author, price))
        self.save_data()
        print("\n Book added successfully!\n")

    # Update book details
    def update_book(self):
        book_id = input("Enter Book ID to update: ")
        for book in self.books:
            if book.book_id == book_id:
                print("\nEnter new details (leave blank to keep old value):")
                name = input(f"Enter new name [{book.name}]: ") or book.name
                author = input(f"Enter new author [{book.author}]: ") or book.author
                price = input(f"Enter new price [{book.price}]: ") or book.price
                book.name, book.author, book.price = name, author, price
                self.save_data()
                print("\n Book updated successfully!\n")
                return
        print("\n Book not found!\n")

    # Delete a book
    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_data()
                print("\nBook deleted successfully!\n")
                return
        print("\n Book not found!\n")

    # Show specific data using Regular Expression
    def show_specific_data(self):
        print("\n1. Show Names")
        print("2. Show Authors")
        print("3. Show Prices")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            pattern = r".*"
            print("\n Book Names:")
            for book in self.books:
                if re.match(pattern, book.name, re.IGNORECASE):
                    print(f"- {book.name}")
        elif choice == "2":
            pattern = r".*"
            print("\n Authors:")
            for book in self.books:
                if re.match(pattern, book.author, re.IGNORECASE):
                    print(f"- {book.author}")
        elif choice == "3":
            pattern = r".*"
            print("\n Prices:")
            for book in self.books:
                if re.match(pattern, str(book.price)):
                    print(f"- {book.price}")
        else:
            print("\n Invalid choice!")

    # Show all data
    def show_all_data(self):
        if not self.books:
            print("\nNo books available!\n")
            return
        print("\n All Books:\n")
        for book in self.books:
            print(book)


# ---------------- MAIN PROGRAM ----------------
def main():
    store = BookStore()

    while True:
        print("\n====== BOOK STORE MENU ======")
        print("1. Add New Book")
        print("2. Update Book Data")
        print("3. Delete Book")
        print("4. Show Specific Data (using Regex)")
        print("5. Show All Data")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            store.add_book()
        elif choice == "2":
            store.update_book()
        elif choice == "3":
            store.delete_book()
        elif choice == "4":
            store.show_specific_data()
        elif choice == "5":
            store.show_all_data()
        elif choice == "6":
            print("\n Exiting... Data saved successfully!")
            break
        else:
            print("\n Invalid choice! Try again.")

if __name__ == "__main__":
    main()
