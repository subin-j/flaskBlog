from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_login import LonginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc838d483ea15b50860be587d0554b79'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_view_messege_category ='info'

# module 'routes'has to be imported after app declaration. (else,circular error)
from flaskblog import routes