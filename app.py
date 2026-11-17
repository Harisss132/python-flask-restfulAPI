from flask import Flask
from flask_cors import CORS
from flask_restplus import Api

from config import Config
from db_config import test_connection, users_collection
from namespace.book_ns import book_ns
from namespace.auth_namespace import api as auth_ns

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

api = Api(
    app,
    version="1.0",
    title="Book Management API",
    description="REST API for managing books"
)

api.add_namespace(book_ns, path="/api/books")
api.add_namespace(auth_ns, path="/api/auth")

@app.route("/")
def index():
    return {
        "message": "Book API is running"
    }


if __name__ == "__main__":
    test_connection()
    users_collection.create_index("google_id", unique=True)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
