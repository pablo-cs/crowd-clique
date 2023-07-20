from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)


app.route('/')(login)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")