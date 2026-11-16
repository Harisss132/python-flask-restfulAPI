from pymongo import MongoClient
from pymongo.errors import PyMongoError

from config import Config

client = MongoClient(
    Config.MONGO_URI,
    serverSelectionTimeoutMS=5000
)

db = client["chapter3_db"]

books_collection = db["books"]
users_collection = db["users"]


def test_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")

    except PyMongoError as error:
        print(f"MongoDB connection failed: {error}")
        raise
