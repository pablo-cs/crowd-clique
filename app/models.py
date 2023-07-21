from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), unique=True, nullable=False)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  pronouns =db.Column(db.String(60), nullable=False)


  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

