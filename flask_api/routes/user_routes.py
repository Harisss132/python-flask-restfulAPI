from flask import Blueprint
from controllers.user_controller import get_all_users, create_user, update_user, delete_user, get_user

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(get_all_users)
user_bp.route('/', methods=['POST'])(create_user)
user_bp.route('/<int:user_id>', methods=['PUT'])(update_user)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user)
user_bp.route('/<int:user_id>', methods=['GET'])(get_user)