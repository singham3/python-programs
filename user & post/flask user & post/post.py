from flask import Flask,render_template, request,flash, redirect, render_template, request, session, abort
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/login_flask'
db = SQLAlchemy(app)


class Login(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100),)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    conform_password = db.Column(db.String(20), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        username = request.form.get('username')
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        conform_password = request.form.get('conform_password')
        print(username,full_name,email,password,conform_password)
        entry = Login(username = username,full_name = full_name,email = email,password = password,conform_password = conform_password)
        print(entry)
        db.session.add(entry)
        db.session.commit()
    return render_template('login_signup.html')


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

if __name__ == '__main__':
    app.run(debug=True)