from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True)
  password = db.Column(db.String(64))
  platforms = db.relationship('Platform')
  games = db.relationship('Game')

class Platform(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(64))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  games = db.relationship('Game')

class Game(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  format = db.Column(db.String(16))
  completion = db.Column(db.String(16))
  backlogged = db.Column(db.String(8))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))