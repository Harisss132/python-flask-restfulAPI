from flask_restplus import fields


def register_book_model(namespace):

    book_model = namespace.model("Book", {
        "id": fields.String(readonly=True),
        "title": fields.String(
            required=True,
            description="Book Title"
        ),
        "author": fields.String(
            required=True,
            description="Book author"
        ),
        "year": fields.String(
            required=True,
            description="Publication year"
        )
    })

    return book_model
