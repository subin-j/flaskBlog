from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Jade J',
        'title':'blog post 1',
        'content': 'first content',
        'date_posted': '00-00-21'
    },
    {
        'author' : 'Jojo J',
        'title':'blog post 2',
        'content': 'second content',
        'date_posted': '00-00-21'
    }
]

@app.route("/")
def home():
    return render_template('home.html',posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html')
