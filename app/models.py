from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  pronouns =db.Column(db.String(60), nullable=False)
  avatar = db.Column(db.String(255), nullable = False)


  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

#to store the comments for an event
class CommentEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, unique=False, nullable = False)
    user_name = db.Column(db.String(20), unique = False, nullable = False)
    comment = db.Column(db.String(255), unique=False, nullable = False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id')) #replies to each comment
    replies = db.relationship(
        'Comment', backref=db.backref('parent', remote_side=[id]),
        lazy='dynamic')

    def add_reply(self, text):
        return Comment(text=text, parent=self)

    #to check getting right info
    def __repr__(self):
        return f"Player('{self.event_id}',{self.event_name},{self.user_name},{self.comment})"





