from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm, ContactForm
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import pandas as pd
import redis_test
# from dash_app import create_dash_app
# create_dash_app(app)

@app.route('/lol',methods=['GET', 'POST'])
@login_required
def get_message():
    message = requests.get('http://app2:4000/return_message')
    return message.text
    # import urllib3
    #
    # http = urllib3.PoolManager()
    # r = http.request('GET', 'http://www.kallithea.gr')
    # # r.status
    # message = r.data
    # # message = requests.get('http://localhost:4000')
    # return message
@app.route('/user',methods=['GET', 'POST'])
@login_required
def get_message_2():
    message = requests.get('http://app3:4001/return_message')
    return message.text

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    email=form.email.data
    # url = 'http://127.0.0.1:3000/lol'
    # myobj = {'somekey': 'somevalue'}
    if email is not None:
        # data = [email]
        # df  = pd.DataFrame(data)
        # df.to_csv('mail.csv')
        redis_test.redis_in(email)
        return redirect(url_for('do_foo', messages=email))

    # requests.post(url, data = myobj)
    return render_template('home.html',message=f'Please insert your email to receive recommendations.',form=form)

@app.route('/foo', methods=['GET', 'POST'])
@login_required
def do_foo():
    message = requests.get('http://send:3000')
    return message.text


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            # if next == None or not next[0]=='/':
            #     next = url_for('get_message')
            print(user)
            print(type(user))
            if next == None or not next[0]=='/':
                if str(user) == '<User 12>':
                    next = url_for('get_message')
                else:
                    next = url_for('get_message_2')

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)
