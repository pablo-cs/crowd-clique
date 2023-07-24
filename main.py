from flask import Flask, render_template, request, redirect, url_for
from flask_behind_proxy import FlaskBehindProxy
from app.models import db
from app.routes import login, signup, home, event_landing, search, err, add_comment, add_reply, event_comments, event_replies,add_attendee


app = Flask(__name__, static_folder="app/static", template_folder="app/templates")
proxied = FlaskBehindProxy(app)
app.secret_key ='bae5f8bb14e95a28a1d679fe833a7ba2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)
with app.app_context():
  db.create_all()

app.route('/',methods=['GET', 'POST'])(home)
app.route('/login',methods=['GET', 'POST'])(login)
app.route('/signup',methods=['GET', 'POST'])(signup)
app.route('/search', methods=['POST'])(search)  # Specify the allowed methods for the route
app.route('/event_landing')(event_landing)
app.route('/err')(err)
app.route('/add_comment',methods=['POST'])(add_comment)
app.route('/add_reply',methods=['POST'])(add_reply)
app.route('/event_comments',methods=['GET', 'POST'])(event_comments)
app.route('/event_replies',methods=['GET', 'POST'])(event_replies)
app.route('/add_attendee',methods=['GET', 'POST'])(add_attendee)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")