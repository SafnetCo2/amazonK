from flask import request, jsonify
from app import db
from app.models import User
from flask import current_app as app

@app.route('/users', methods=['GET'])
def list_user():
    try:
        users = User.query.all()
        if not users:
            return jsonify({
                "status": "success",
                "message": "No users found."
            }), 200

        user_data = [user.to_dict() for user in users]
        return jsonify({
            "status": "success",
            "data": user_data
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
