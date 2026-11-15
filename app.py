from flask import Flask
from flask_restplus import Api

from db_config import test_connection
from namespace.book_ns import book_ns

app = Flask(__name__)

api = Api(
    app,
    version="1.0",
    title="Book Management API",
    description="REST API for managing books"
)

api.add_namespace(book_ns, path="/api/books")

@app.route("/")
def index():
    return {
        "message": "Book API is running"
    }


if __name__ == "__main__":
    test_connection()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
