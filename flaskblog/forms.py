from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo, ValidationError 
import email_validator


#------------------------Register
class RegistrationForm(FlaskForm):
    email = StringField(
        'Email', validators = [DataRequired(), Email()]
    )    
    username = StringField(
        #validates string input username -is not null and set minmax length with DataRequired and Length modules.
        'Username', validators = [DataRequired(), Length(min=1, max=20)]
    )
    password = PasswordField(
        'Password', validators = [DataRequired()]
    )        
    confirm_password = PasswordField(
        'Confirm Password',validators = [DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')
    #raise ValidationError when username and email have duplicates
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. please choose a difference username.')
            
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. please choose a difference username.')
            
#------------------------Login
class LoginForm(FlaskForm):
    email = StringField(
        'Email', validators = [DataRequired(), Email()]
    )
    password =  PasswordField(
        'Password', validators = [DataRequired()]
    )
    remember = BooleanField(
        'Remember Me'
        )
    submit = SubmitField(
        'Sign in'
        )
