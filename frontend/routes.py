from frontend import app
from flask import render_template, redirect, flash, url_for
from frontend.forms import LoginForm, RegistrationForm, CommandForm
from flask_login import current_user, login_user, logout_user
from frontend.models import User
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from frontend import db
from backend import processanswer
from backend.webservices.formservices import *

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/command', methods=['GET', 'POST'])
@login_required
def command():
    form = CommandForm()
    if form.validate_on_submit():
        name = current_user.username
        answer = form.command.data
        response = processanswer.processAnswerWebSite(name, answer)
        if response != None:
            flash(response)
    return render_template('command.html', title='Command', form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/rum')
def rum():
    return render_template('rum.html', title='Rum')