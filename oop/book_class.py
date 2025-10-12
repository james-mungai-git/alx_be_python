class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation"""
        return f"'{self.title}' by {self.author} ({self.year})"

    def __repr__(self):
        """Developer-friendly string representation"""
        return f"Book({self.title!r}, {self.author!r}, {self.year!r})"

    def __del__(self):
        """Called when the object is deleted"""
        print(f"Book '{self.title}' by {self.author} has been removed from memory.")

