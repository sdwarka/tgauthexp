from flask_login import UserMixin
from app import db

# Flask-login can manage user sessions through the UserMixin class.
# This will add flask-login attributes to the model for flask-login
# to be able to work with it.
#
# See routes.py @login_manager for continuation of this

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

