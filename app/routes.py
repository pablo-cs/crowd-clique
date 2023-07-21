from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy

from app.forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from app.ticketmaster_api import search_events
app = Flask(__name__)
proxied = FlaskBehindProxy(app) 
app.config['SECRET_KEY'] = '117b3274820db891a19981c6ab2a0fd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def home():
    return render_template('index.html')
    
def login():
    form = LoginForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return flash(f'Account created for {form.username.data}!', 'success')
        flash(f'Account created for {form.username.data}!', 'success')
    return render_template('login.html', title='Log In', form=form)

def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return flash(f'Account created for {form.username.data}!', 'success')
        flash(f'Account created for {form.username.data}!', 'success')
    return render_template('signup.html', title='Sign Up', form=form)

def event_landing():
    events = search_events("concert")
    return render_template('event_landing.html', events=events)

