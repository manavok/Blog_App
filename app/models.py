from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, index = True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"User: {self.username}."
    
    @property
    def password(self):
        raise AttributeError('password Nahi Dekna Lallu!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)