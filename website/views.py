from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Platform, Game
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def root():
    if current_user.is_authenticated:
        return redirect(url_for('views.gaming_backlog_manager'))

    return redirect(url_for('auth.login'))

@views.route('/gaming-backlog-manager', methods=['GET', 'POST'])
@login_required
def gaming_backlog_manager():
    return render_template('gaming_backlog_manager.html', user=current_user)

@views.route('/platforms', methods=['GET', 'POST'])
@login_required
def platforms():
    if request.method == 'POST':
        platform = request.form.get('platform')
        if len(platform) < 1:
            flash('Platform field is empty!', category='danger')
        elif len(platform) > 64:
            flash('Platform name is too long!', category='danger')
        else:
            new_platform = Platform(title=platform, user_id=current_user.id)
            db.session.add(new_platform)
            db.session.commit()
            flash('Platform added successfully!', category='success')

    return render_template('platforms.html', user=current_user)

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