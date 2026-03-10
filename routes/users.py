from flask import Blueprint, request
from models import User
from database import db

users = Blueprint("users", __name__)

@users.route("/users", methods=["POST"])
def create_user():

    data = request.json

    user = User(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User created"}