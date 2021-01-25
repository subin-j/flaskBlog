from datetime import datetime
# after refactoring, 'flaskblog' is now a package.
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#------------DB classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer ,primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    # posts backref author attirubute.(1toM relationsip)/ lazy-load
    posts = db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer ,primary_key=True, nullable=False)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow) #import Datetime module
    content = db.Column(db.Text, nullable=False)
    # user.id.User is foreign key of user_id.Post
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

