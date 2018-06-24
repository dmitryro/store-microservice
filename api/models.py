from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ =  'orders'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=False)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    state = db.Column(db.String(2), nullable=True)
    zipcode = db.Column(db.String(9), nullable=True)

    valid = db.Column(db.Boolean, default=True)
    errors = db.Column(db.Text, nullable=True)

    def __init__(self, *args, **kwargs):
        for field in kwargs:
            setattr(self, field, kwargs[field])

    def __repr__(self):
        return '<Order %d>' % self.id

