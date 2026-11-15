from db_config import books_collection


class BookService:

    @staticmethod
    def create_book(data):
        result = books_collection.insert_one(data.copy())

        return {
            "id": str(result.inserted_id),
            **data
        }

    @staticmethod
    def get_all_books():
        books = books_collection.find()

        result = []

        for book in books:
            book["id"] = str(book.pop("_id"))
            result.append(book)

        return result
