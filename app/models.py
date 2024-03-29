from app import login
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import JSON


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Reunion(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_num = db.Column(db.String(8), nullable=False)
    hippodrome = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    quinte = db.Column(db.Integer)

