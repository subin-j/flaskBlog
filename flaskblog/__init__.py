from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#forms 에서 클래스를 임포트 하지 않으면 app파일이 인식하지 않는다.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc838d483ea15b50860be587d0554b79'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# module 'routes'has to be imported after app declaration. (else,circular error)
from flaskblog import routes