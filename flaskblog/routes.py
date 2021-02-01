from flask import render_template, url_for, flash, redirect, request
from flaskblog import app ,db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAcountForm
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
            next_page = request.args.get('next')
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

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateAcountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated successfully.','success')
        return redirect(url_for('account'))
    elif request.method =='GET':
        # populate current user form with username and email
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    
    return render_template('account.html', title='Account', image_file= image_file, form=form)