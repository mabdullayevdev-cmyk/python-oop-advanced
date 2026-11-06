class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)

    def search_book(self, title: str):
        return [b for b in self.books if title.lower() in b.title.lower()]


class Member:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if not book.is_available:
            raise ValueError(f"'{book.title}' kitobi allaqachon band qilingan!")
        book.is_available = False
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("Bu kitob sizning ro'yxatingizda yo'q!")
        book.is_available = True
        self.borrowed_books.remove(book)


if __name__ == "__main__":
    lib = Library()
    b1 = Book("Python Crash Course", "Eric Matthes")
    lib.add_book(b1)

    member = Member("Akmal")
    member.borrow_book(b1)
    print(f"Kitob mavjudmi? {b1.is_available}")

    member.return_book(b1)
    print(f"Kitob qaytarildi, mavjudmi? {b1.is_available}")