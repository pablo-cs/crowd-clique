from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.routes import login

app = Flask(__name__, template_folder='app/templates')
proxied = FlaskBehindProxy(app)
app.secret_key ='bae5f8bb14e95a28a1d679fe833a7ba2'

app.route("/login", methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")