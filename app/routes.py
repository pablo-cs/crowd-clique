from flask import Flask, render_template, request, redirect, url_for,flash, session
from flask_behind_proxy import FlaskBehindProxy
from app.models import User,db, CommentEvent, Reply
from app.forms import LoginForm, RegistrationForm, CommentForm
from flask_sqlalchemy import SQLAlchemy
from app.ticketmaster_api import search_events, suggest_events, get_event_details
from datetime import datetime

img = {'d': '../static/img/dog.jpg', 'c': '../static/img/cat.jpg','s': '../static/img/sunset.jpg'}


def home():
    return render_template('index.html')

def err():
    return render_template('err.html',subtitle='Oh no!', text='The username and/or password entered is not correct. Please try again or sign up.')

def login():
    form = LoginForm()
    if form.validate_on_submit(): # checks if entries are valid
        user=User.query.filter_by(username=form.username.data).first()
        if user:
            flash(f'Welcome,{form.username.data}!')
            session['username'] = form.username.data
            return redirect(url_for('event_landing'))
        else:
            return redirect(url_for('err'))
    return render_template('login.html', title='Log In', form=form)



def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        user = User(name=form.name.data,username=form.username.data,email=form.email.data,password=form.password.data,pronouns=form.pronouns.data, avatar=img[form.avatar.data])
        session['user_name'] = form.username.data
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


def add_comment():
    user_name = session.get('user_name')
    comment = request.form.get('user_comment')
    event_id = request.form.get('event_id')
    event_details = get_event_details(event_id)
    current_time = datetime.now()
    comment = CommentEvent(event_id=event_id, user_name=user_name, comment=comment, timestamp=current_time)
    db.session.add(comment)
    db.session.commit()
    form = CommentForm()
    event_comments = CommentEvent.query.filter_by(event_id=event_id).all()
    return render_template(
        'event_comments.html',event_details=event_details,
        comments=event_comments,
        form=form
    )

def add_reply():
    user_name = session.get('user_name')
    reply = request.form.get('reply')
    event_id = request.form.get('event_id')
    event_details = get_event_details(event_id)
    comment_id = request.form.get('comment_id')
    #how are we getting comment id
    reply= Reply(comment_id=comment_id,event_id=event_id, user_name=user_name, reply=reply)
    db.session.add(reply)
    db.session.commit()
    form = CommentForm()
    comment_replies = Reply.query.filter_by(comment_id=comment_id).all()
    return render_template(
        'event_replies.html', event_details=event_details, comment_id=comment_id,
        comment_replies=event_replies,
        form=form
    )


def event_comments():
    event_id = request.form.get('event_id')
    event_details = get_event_details(event_id) #gets event object
    #query the comments database for comments with that event id
    event_comments = CommentEvent.query.filter_by(event_id=event_id).all()
    form = CommentForm()
    return render_template('event_comments.html', event_details=event_details,
    event_comments=event_comments,form=form)

def event_replies():
    event_id = request.form.get('event_id')
    comment_id = request.form.get('comment_id')
    event_details = get_event_details(event_id)
    #query database for replies with that comment id
    comment_replies = Reply.query.filter_by(comment_id=comment_id).all()
    form = CommentForm()
    return render_template('event_replies.html', event_details=event_details,comment_id=comment_id,
    replies=comment_replies, form=form)