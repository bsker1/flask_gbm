from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('auth.login'))

@views.route('/home')
def home():
    return render_template("home.html")