from flask import render_template, flash, redirect, url_for
from app import app, db

from app.forms import LoginForm, RegistrationForm
from app.turf_forms import TurfForm


from flask_login import current_user, login_user
from flask_login import logout_user
from app.models import User, Reunion
from flask_login import login_required

from flask import request
from werkzeug.urls import url_parse


from datetime import datetime


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page', active='home')

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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

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
    return render_template('register.html', title='Register', form=form)

@app.route('/turf', methods=['GET', 'POST'])
def turf():
    form = TurfForm()
    form.date.choices = [(reunion.id_num, reunion.date.strftime("%Y/%m/%d")) for reunion in Reunion.query.all()]
    form.hippodrome.choices = [(reunion.id_num, reunion.hippodrome) for reunion in Reunion.query.all()]

    if request.method == 'POST':
        hippodrome = Reunion.query.filter_by(id_num = form.date.data).all()
        return '<h1> Date: {}, Hippodrome: {} </h1>'.format(form.date.data, hippodrome.name)

    # print(form.date.choices)
    # reunions = Reunion.query.limit(1000)
    return render_template("turf.html", title='Turf', active='turf', form = form)
