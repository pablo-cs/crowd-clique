from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy

def login():
    # Assuming you have a 'templates' folder in your project containing the 'login.html' file
    return render_template('login.html')