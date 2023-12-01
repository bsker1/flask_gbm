from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('auth.login'))

@login_required
@views.route('/home')
def home():
    return render_template("home.html", user=current_user)