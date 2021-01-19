from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo 
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
        'Confirm Password',validators = [DataRequired(), EqualTo(password)]
    )
    submit = SubmitField('Sign Up')

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
