from functools import wraps
from flask import request, g
from services.auth_service import AuthError, decode_access_token

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return {"message": "Missing token"}, 401
        try:
            g.current_user = decode_access_token(header.split(" ", 1)[1])
        except AuthError as e:
            return {"message": str(e)}, 401
        return f(*args, **kwargs)

    return wrapper