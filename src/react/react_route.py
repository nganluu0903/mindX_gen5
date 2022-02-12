from flask import Blueprint,request,jsonify
from src.blog.blog import Blog
from src import db
react=Blueprint('react', __name__)
from sqlalchemy import update
@react.route('/react', methods=["POST"])
def log_in():
    blog_id=int(request.args.get('blog_id'))
    reaction= request.args.get('reaction')
    blog=Blog.query.filter_by(id=blog_id).first()
    if blog:
        Blog.reaction=reaction
        db.session.commit()
        return 'React Success'
    else:
        return "Blog not found",404