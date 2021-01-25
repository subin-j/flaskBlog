from flask import render_template, url_for, flash, redirect, request
from flaskblog import app ,db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user,login_required

# fyi , routes= views.

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

        #generate hased password and create user object 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        #add newly created user data and commit to DB
        db.session.add(user)
        db.session.commit()

        #flash messege if success, with bootstrap class 'success'
        flash('Your account has been created!','success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
    #if already logged in, redirect to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # instantiate 'form' from class
    form = LoginForm()
    # validates then alerts & redirect
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        #login success
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = requeest.args.get('next')
            #redirect to next_page if exist, else redirect to 'home'
            return redirect(next_page) if next_page else redirect(url_for('home'))
        #login fail
        else: 
            flash("Login Unsuccessful. Please check the credentials.","danger")
    
    return render_template('login.html', title='Login',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    logout_user()
    return render_template('account.html', title='Account')
