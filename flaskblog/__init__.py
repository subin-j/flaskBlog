from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LonginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc838d483ea15b50860be587d0554b79'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LonginManager(app)

# module 'routes'has to be imported after app declaration. (else,circular error)
from flaskblog import routes