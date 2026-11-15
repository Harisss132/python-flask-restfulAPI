from http import HTTPStatus

from flask_restplus import Namespace, Resource

from schemas.book_schema import register_book_model
from services.book_service import BookService

book_ns = Namespace("books", description="Book operations")
book_model = register_book_model(book_ns)

@book_ns.route("/")
class BookListResource(Resource):

    @book_ns.doc("get_all_books")
    @book_ns.marshal_list_with(book_model)
    def get(self):
        return BookService.get_all_books()

    @book_ns.expect(book_model, validate=True)
    @book_ns.response(201, "Book Successfuly created", book_model)
    @book_ns.marshal_with(book_model)
    def post(self):
        data = book_ns.payload
        result = BookService.create_book(data)

        return result, HTTPStatus.CREATED
