class books:
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self._is_checked_out = False

class library:
	def __init__(self):
		self._books = []

	def add_book(self, title, author):
		for book in self._books:
			if book.title.lower() == title.lower() and book.author.lower() == author.lower():
				print(f"{book.title} by {book.author} already exists in the library list")
				return
		self._books.append(books(title, author))
		print(f"added {title} by {author} to library")

	def check_out_book(self, title, author):
		for book in self._books:
			if book.title.lower() == title.lower() and book.author.lower() == author.lower():
				if book._is_checked_out:
					print(f"{title} has already been checked out")
					return
				book._is_checked_out = True
				print(f"{title} by {author} has been checked out")
				return
		print(f"{title} by {author} not found in the library")
	
	def return_book(self, title, author):
		for book in self._books:
			if book.title.lower() == title.lower() and book.author.lower() == author.lower():
				if not book._is_checked_out:
					print(f"{title} had not been checked out")
					return
				book._is_checked_out = False
				print(f"{title} has been returned")
				return
		print(f"{title} was not found in the library")

	def list_available_books(self):
		if not self._books:
			print("list is empty")
			return
		for index, book in enumerate(self._books, start=1):
			status = "checked out" if book._is_checked_out else "available"
			print(f"{index}. {book.title} by {book.author} - {status}")
			
	def library_menu(self):
		print("\n ---library menu---")
		print("1. Add book")
		print("2. Check out book")
		print("3. return a book")
		print("4. View library list")
		print("5. Exit")
		
# main loop

# ...existing code...

def main():
    lib = library()
    
    while True:
        lib.library_menu()
        choice = input("Pick a number between 1 and 5: ")

        if choice == "1":
            title = input("Enter the title of the book you wish to add: ")
            author = input("Enter the name of the author: ")
            lib.add_book(title, author)

        elif choice == "2":
            title = input("Enter the title of the book you wish to check out: ")
            author = input("Enter the name of the author: ")
            lib.check_out_book(title, author)

        elif choice == "3":
            title = input("Enter the title of the book you wish to return: ")
            author = input("Enter the name of the author: ")
            lib.return_book(title, author)

        elif choice == "4":
            lib.list_available_books()  # fixed: added parentheses to call the method

        elif choice == "5":
            print("Thank you for using our services, come again!")
            break

        else:
            print("Invalid input, kindly enter again")

if __name__ == "__main__":  # fixed: corrected __name__ check
    main()

				
			




    			



				