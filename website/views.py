from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Platform, Game
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def root():
    return redirect(url_for('auth.login'))

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    """
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is empty!', category='danger')
        else:
            new_note = Note(content=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    """

    return render_template('home.html', user=current_user)

@views.route('/add-platform', methods=['GET', 'POST'])
@login_required
def add_platform():
    if request.method == 'POST':
        platform = request.form.get('platform')
        if len(platform) < 1:
            flash('Platform field is empty!', category='danger')
        else:
            new_platform = Platform(title=platform, user_id=current_user.id)
            db.session.add(new_platform)
            db.session.commit()
            flash('Platform added successfully!', category='success')

    return render_template('add_platform.html', user=current_user)

@views.route('/delete-platform', methods=['POST'])
def delete_platform():
    platform = json.loads(request.data)
    platformId = platform['platformId']
    platform = Platform.query.get(platformId)
    if platform:
        if platform.user_id == current_user.id:
            db.session.delete(platform)
            db.session.commit()
    
    return jsonify({})

@views.route('/delete-game', methods=['POST'])
def delete_game():
    game = json.loads(request.data)
    gameId = game['gameId']
    game = Game.query.get(gameId)
    if game:
        if game.user_id == current_user.id:
            db.session.delete(game)
            db.session.commit()
    
    return jsonify({})