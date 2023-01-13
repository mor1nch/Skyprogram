from flask import Blueprint, jsonify
from utils import *

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/api/posts")
def get_posts_json():
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route("/api/posts/<int:post_id>")
def get_post_json(post_id):
    post = get_post_by_post_id(post_id)
    return jsonify(post)
