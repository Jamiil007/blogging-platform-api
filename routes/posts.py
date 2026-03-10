from flask import Blueprint, request
from models import Post
from database import db

posts = Blueprint("posts", __name__)

@posts.route("/posts", methods=["POST"])
def create_post():

    data = request.json

    post = Post(
        title=data["title"],
        content=data["content"],
        author_id=data["author_id"]
    )

    db.session.add(post)
    db.session.commit()

    return {"message": "Post created"}