from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.routes import login

app = Flask(__name__, template_folder='app/templates')
proxied = FlaskBehindProxy(app)


app.route('/')(login)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")