from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.models import db
from app.routes import login, signup, home, event_landing, search

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
proxied = FlaskBehindProxy(app)
app.secret_key ='bae5f8bb14e95a28a1d679fe833a7ba2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
<<<<<<< HEAD

=======
>>>>>>> f035947855d120a38a1fe47f5f9fb22ad9e47c15
db.init_app(app)
with app.app_context():
  db.create_all()

app.route('/',methods=['GET', 'POST'])(home)
app.route('/login',methods=['GET', 'POST'])(login)
app.route('/signup',methods=['GET', 'POST'])(signup)
<<<<<<< HEAD
app.route('/search', methods=['POST'])(search)  # Specify the allowed methods for the route
=======
app.route('/search', methods=['POST'])(search)
>>>>>>> f035947855d120a38a1fe47f5f9fb22ad9e47c15
app.route('/event_landing')(event_landing)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")