from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.routes import login,signup
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  pronouns =db.Column(db.String(60), nullable=False)


  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

#to store the comments for an event
class CommentEvent(db.Model):
    __bind_key__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, unique=False, nullable = False)
    event_name = db.Column(db.String(50),unique=False, nullable = False)
    user_name = db.Column(db.String(20), unique = False, nullable = False)
    comment = db.Column(db.String(255), unique=False, nullable = False)

    #to check getting right info
    def __repr__(self):
        return f"Player('{self.event_id}',{self.event_name},{self.user_name},{self.comment})"

#replies to each comment
class Replies(db.Model):
    __bind_key__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, unique=False, nullable = False)
    user_name = db.Column(db.String(20), unique = False, nullable = False)
    reply = db.Column(db.String(255), unique=False, nullable = False)



