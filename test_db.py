from db_config import books_collection

book = {
    "title": "The Pragmatic Programmer",
    "author": "Andrew Hunt",
    "year": 1999
}

result = books_collection.insert_one(book)
print("Insert ID:", result.inserted_id)
