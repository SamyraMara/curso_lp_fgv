from typing import List

class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title : str = title
        self.author : str = author
        self.isbn : str = isbn
    
    def __str__(self) -> str:
        return f"Titulo: {self.title}\nAutor: {self.author}\nISBN: {self.isbn}"

class Library:
    def __init__(self) -> None:
        self.books : List[Book] = []

    

    def add_book(self, book: Book) -> None:
        if book is None:
            raise  ValueError("Nao foi passado nenhum livro")
        if self.search_isbn(book.isbn) is not None:
            return
        self.books.append(book)
    
    def remove_book(self, isbn: str) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                break

    def search_isbn(self, isbn: str) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book
            
        return None   

    
    

class LibraryApp:
    def __init__(self):
        self.library = Library()

    def run(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search by Title")
            print("4. Search by Author")
            print("5. List All Books")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                self.library.add_book(Book(title, author, isbn))

            elif choice == '2':
                isbn = input("Enter book ISBN to remove: ")
                self.library.remove_book(isbn)

            elif choice == '3':
                title = input("Enter book title to search: ")
                books = self.library.search_by_title(title)
                if books:
                    for book in books:
                        print(book)
                else:
                    print('No books found with that title.')

            elif choice == '4':
                author = input("Enter author name to search: ")
                books = self.library.search_by_author(author)
                if books:
                    for book in books:
                        print(book)
                else:
                    print('No books found by that author.')

            elif choice == '5':
                self.library.list_books()

            elif choice == '6':
                print('Exiting...')
                break

            else:
                print('Invalid choice, please try again.')


if __name__ == "__main__":
    app = LibraryApp()
    app.run()