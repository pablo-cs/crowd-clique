from flask import Flask, render_template, request, redirect, url_for,flash
from flask_behind_proxy import FlaskBehindProxy
from app.models import User,db
from app.forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from app.ticketmaster_api import search_events, suggest_events



def home():
    return render_template('index.html')
    
def login():
    form = LoginForm()
    if form.validate_on_submit(): # checks if entries are valid
        user=User.query.filter_by(username=form.username.data).first_or_404(description='There is no data with {}'.format(form.username.data))
        # print(form.username.data)
        flash(f'Welcome,{form.username.data}!')
        return redirect(url_for('event_landing'))
    return render_template('login.html', title='Log In', form=form)

def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(name=form.name.data,username=form.username.data,email=form.email.data,password=form.password.data,pronouns=form.pronouns.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('event_landing'))
    return render_template('signup.html', title='Sign Up', form=form)

def event_landing():
    events = suggest_events()
    return render_template('event_landing.html', your_events=[], suggested_events=events)

def search():
    search_query = request.form.get('search')
    if search_query:
        search_results = search_events(search_query)
        if len(search_results) > 0:
            return render_template(
                    'search_result.html', search_results=search_results
                )
    return render_template('search_result.html', search_results=None)