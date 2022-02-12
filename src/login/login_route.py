from flask import Blueprint,request,jsonify
from src.user.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash,generate_password_hash
from src import db
login=Blueprint('login', __name__)

@login.route('/login', methods=["POST"])
def log_in():
    email=request.args.get('email')
    password = request.args.get('password')
    user=User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password,password):
            jwt_token=create_access_token(identity=user.email)
            return jsonify({"token":jwt_token})
    else:
        return "Invalid email or password",400
@login.route('/sign_up', methods=["POST"])
def sign_up():
    email = request.args.get('email')
    password = generate_password_hash(request.args.get('password'))
    user = User.query.filter_by(email=email).first()
    if user:
        return 'Account already exists',400
    else:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'Sign up success {}'.format(email),200