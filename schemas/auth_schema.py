from flask_restplus import fields

def build_auth_models(api):
    google_login_request = api.model("GoogleLoginRequest", {
        "id_token": fields.String(required=True)
    })
    user_model = api.model("User", {
        "id": fields.String,
        "email": fields.String,
        "name": fields.String,
        "picture": fields.String
    })
    login_response = api.model("LoginResponse", {
        "access_token": fields.String,
        "user": fields.Nested(user_model)
    })
    return google_login_request, login_response