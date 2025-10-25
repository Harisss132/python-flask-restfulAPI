from flask import jsonify, request
from config.db_config import db
from models.user_models import User

def get_all_users():
    users = User.query.all()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)

def get_user(user_id):
    user = User.query.get(user_id)
    result = [{"id": user.id, "name": user.name, "email": user.email}]
    return jsonify(result)

def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "user created", "user": {"id": new_user.id, "name": new_user.name}})

def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify({"message": "User updated", "user": {"id": user.id, "name": user.name}})

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user_id} deleted"})