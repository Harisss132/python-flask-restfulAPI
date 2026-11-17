from flask import request, g
from flask_restplus import Namespace, Resource

from schemas.auth_schema import build_auth_models
from services.auth_decorator import login_required
from services.auth_service import (
    AuthError, create_access_token, upsert_user, verify_google_token
)

api = Namespace("auth", description="Authentication")
google_login_request, login_response = build_auth_models(api)

@api.route('/google')
class GoogleLogin(Resource):
    @api.expect(google_login_request, validate=True)
    @api.response(200, "Success", login_response)
    def post(self):
        token = request.get_json()["id_token"]
        try:
            info = verify_google_token(token)
        except AuthError as e:
            return {"message": str(e)}, 401

        user = upsert_user(info)
        return {
            "access_token": create_access_token(user),
            "user": {
                "id": str(user["_id"]),
                "email": user["email"],
                "name": user.get("name"),
                "picture": user.get("picture")
            },
        }, 200

@api.route('/me')
class Me(Resource):
    @login_required
    def get(self):
        return {"user_id": g.current_user["sub"], "email": g.current_user["email"]}, 200