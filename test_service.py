from services.book_service import BookService

book = {
    "title": "The tetris pragmatic",
    "author": "Andrew tate",
    "year": 2000
}

create_book = BookService.create_book(book)
print("created:", create_book)
all_books = BookService.get_all_books()
print("All Books:",all_books)
