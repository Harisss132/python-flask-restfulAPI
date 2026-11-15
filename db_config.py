from pymongo import MongoClient
from pymongo.errors import PyMongoError

MONGO_URI = "mongodb://127.0.0.1:27017"

client = MongoClient(
    MONGO_URI,
    ServerSelectionTimeoutMs=5000
)

db = client["chapter3_db"]

books_collection = db["books"]

def test_connection():
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")

    except PyMongoError as error:
        print(f"MongoDB connection failed: {error}")
        raise
