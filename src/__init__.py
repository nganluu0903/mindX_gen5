from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Should allow for users to sign up and login.
# Should allow for users to create and post a blog, having author name, tags and created_at
# Should allow users to get all blogs in the new feed
# Should allow users to react user’s blog like heart or like

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
CORS(app)
db.init_app(app)
app.config['JWT_SECRET_KEY']='abc@abc'
jwt=JWTManager(app)
from src.blog.blog_routes import blogs
app.register_blueprint(blogs)
from src.login.login_route import login
app.register_blueprint(login)
from src.react.react_route import react
app.register_blueprint(react)
with app.app_context():
    db.create_all()
@app.route('/',methods=['GET'])
def home():
    return 'MINDX_BLOG_API'
if __name__ == '__main__':
    app.run(debug=True)



