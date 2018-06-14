from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    gender = db.Column(db.String(32))
    phone = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    role_id = db.Column('Role', db.Integer, db.ForeignKey('role.id'))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User: {} {}, {}>'.format(self.firstname, self.lastname, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Role(object):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), index=True)
    role_member = db.relationship('User', backref='role_member', lazy='dynamic')

    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True)
#     description = db.Column(db.String(140))
