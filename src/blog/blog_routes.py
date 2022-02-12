from flask import Blueprint,request,jsonify
from src import db
from src.blog.blog import Blog
from datetime import datetime
# from blog import Blog

blogs = Blueprint('blogs', __name__)
@blogs.route('/post_blog', methods=["POST"])
def create_blog():
    title=request.args.get('title')
    content=request.args.get('content')
    author=request.args.get('author')
    tag=request.args.get('tag')
    new_blog = Blog(title=title, content=content, author=author,tag=tag)
    db.session.add(new_blog)
    db.session.commit()
    blog_id = getattr(new_blog, "id")
    return jsonify({'id':blog_id,\
                    'title': title,\
                    'author':author,\
                    'tag':tag,\
                    'content':content})

@blogs.route('/get_all_blogs', methods=["GET"])
def get_all_blogs():
    data = []
    for blog in Blog.query.all():
        data.append(blog.serialize)
    return jsonify({"Blogs": data})
