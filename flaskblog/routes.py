from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

#----------sample DB
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


#----------------------routing

@app.route("/")
def home():
    return render_template('home.html',posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def register():
    # instantiate 'form' from class
    form = RegistrationForm()
    # validates then alerts
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    # instantiate 'form' from class
    form = LoginForm()
    # validates then alerts & redirect
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='1234':
            flash(f"Logged in successfully!","success")
            return redirect(url_for('home'))

        else: 
                flash("Login Unsuccessful.","danger")
    return render_template('login.html', title='Login',form=form)

