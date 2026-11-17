import datetime

import jwt
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token

from config import Config
from db_config import users_collection

class AuthError(Exception):
    pass

def verify_google_token(token):
    try:
        info = id_token.verify_oauth2_token(
            token, google_requests.Request(), Config.GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise AuthError("Invalid Google token")

    if not info.get("email_verified"):
        raise AuthError("Google email is not verified")
    return info

def upsert_user(info):
    now = datetime.datetime.utcnow()
    users_collection.update_one(
        {"google_id": info["sub"]},
        {
            "$set": {
                "email": info["email"],
                "name": info.get("name"),
                "picture": info.get("picture"),
                "last_login": now,
            },
            "$setOnInsert": {"created_at": now}
        },
        upsert=True
    )
    return users_collection.find_one({"google_id": info["sub"]})

def create_access_token(user, hours=1):
    now = datetime.datetime.utcnow()
    payload = {
        "sub": str(user["_id"]),
        "email": user["email"],
        "iat": now,
        "exp": now + datetime.timedelta(hours=hours),
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

def decode_access_token(token):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthError("Token Expired")
    except jwt.InvalidTokenError:
        raise AuthError("Invalid token")