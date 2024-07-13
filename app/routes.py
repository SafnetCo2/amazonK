from flask import request,jsonify
from app import db
from app.models import User
from flask import current_app as app


@app.route('/users',methods=['GET'])
def list_user():
    users=User.query.all()
    user_data=[user.to_dict()for user in users]
    return jsonify({
        "status":"success in listing users",
        "data":user_data
    }),201
    