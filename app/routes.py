from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
proxied = FlaskBehindProxy(app) 
app.config['SECRET_KEY'] = '117b3274820db891a19981c6ab2a0fd2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def login():
    # Assuming you have a 'templates' folder in your project containing the 'login.html' file
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return flash(f'Account created for {form.username.data}!', 'success')
    return render_template('login.html', title='Log In', form=form)