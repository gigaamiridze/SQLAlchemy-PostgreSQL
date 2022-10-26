from .extensions import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"User: {self.name} {self.surname}"