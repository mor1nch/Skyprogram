import json


def get_posts_all():
    with open("data/posts.json") as file:
        posts_data = json.load(file)
        return posts_data


def get_bookmarks_all():
    with open("data/bookmarks.json") as file:
        bookmarks_data = json.load(file)
        bookmarks = []
        for i in bookmarks_data:
            bookmarks.append(i)
        return bookmarks


def get_comments_all():
    with open("data/comments.json") as file:
        comments_data = json.load(file)
        return comments_data


def get_posts_by_user(user_name):
    posts_by_username_list = []
    posts_data = get_posts_all()
    try:
        for user in posts_data:
            if user["poster_name"] == user_name.lower():
                posts_by_username_list.append(user)
        return posts_by_username_list
    except ValueError:
        return []


def get_comments_by_post_id(post_id):
    comments_by_post_id_list = []
    comments_data = get_comments_all()
    try:
        for comment in comments_data:
            if comment["post_id"] == post_id:
                comments_by_post_id_list.append(comment)
        return comments_by_post_id_list
    except ValueError:
        return []


def get_post_by_post_id(post_id):
    posts_data = get_posts_all()
    try:
        for post in posts_data:
            if post["pk"] == post_id:
                return post
    except ValueError:
        return []


def search_for_posts(query):
    posts_by_query_list = []
    posts_data = get_posts_all()
    for post in posts_data:
        if query.lower() in post["content"].lower():
            posts_by_query_list.append(post)
    return posts_by_query_list

