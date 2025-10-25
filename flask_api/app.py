from flask import Flask
from config.db_config import app as db_app, db
from routes.user_routes import user_bp
from models.user_models import User

app = db_app

app.register_blueprint(user_bp, url_prefix='/api/users')

with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    return{ "message": "Flask rest api connected to postgresql"}

if __name__ == '__main__':
    app.run(debug=True)