from flask import Flask, render_template, request
from api import api_blueprint
from utils import *
import logging

app = Flask(__name__)
app.register_blueprint(api_blueprint)
logging.basicConfig(filename="logs/api.log", level=logging.INFO, filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")


@app.route("/")
def page_main():
    posts = get_posts_all()
    bookmarks = get_bookmarks_all()
    logging.info("Запрос /")
    return render_template("index.html", posts=posts, bookmarks=bookmarks)


@app.route("/posts/<int:postid>")
def page_post(postid):
    comments = get_comments_by_post_id(postid)
    post = get_post_by_post_id(postid)
    logging.info(f"Запрос /posts/{postid}")
    return render_template("post.html", comments=comments, post=post)


@app.route("/search/")
def page_search():
    word = request.args.get('s')
    posts = search_for_posts(word)
    logging.info("Запрос /search/")
    return render_template("search.html", posts=posts)


@app.route("/users/<username>")
def page_user(username):
    posts = get_posts_by_user(username)
    logging.info(f"Запрос /users/{username}")
    return render_template("user-feed.html", posts=posts)


@app.errorhandler(404)
def not_found_error(error):
    return "Error 404, такой страницы не существует"


@app.errorhandler(500)
def internal_error(error):
    return "Error 500, ошибка сервера"


app.run()
