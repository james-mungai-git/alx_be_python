class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked out"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        for book in self._books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print("This book already exists in the library.")
                return
        self._books.append(Book(title, author))
        print(f"{title} by {author} has been added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.check_out()
                    print(f"{title} has been checked out.")
                    return
                else:
                    print(f"{title} is already checked out.")
                    return
        print("Book not found in the library.")

    def display_books(self):
        if not self._books:
            print("Library is empty.")
        else:
            print("\nBooks in the library:")
            for book in self._books:
                print(book)

    def show_menu(self):
        print("\nLibrary Manager")
        print("1. Add book")
        print("2. Check out book")
        print("3. View library list")
        print("4. Exit")


# -------------------------
# Main Program Loop
# -------------------------
def main():
    lib = Library()
    while True:
        lib.show_menu()
        choice = input("Enter a number between 1-4: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            lib.add_book(title, author)

        elif choice == "2":
            title = input("Enter book title to check out: ")
            lib.check_out_book(title)

        elif choice == "3":
            lib.display_books()

        elif choice == "4":
            print("Thank you for using the Library Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

