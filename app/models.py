from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    manga_count = db.Column(db.Integer, default=0)
    password = db.Column(db.String(200), nullable=False)
    mangas = db.relationship('Manga', backref='uploader', lazy=True)

class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uploaded_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
    manga_name = db.Column(db.String(100), nullable=False)
    manga_author = db.Column(db.String(100), nullable=False)
    manga_tags = db.Column(db.String(100), nullable=False)
    manga_issue_no = db.Column(db.Integer, nullable=False)
    manga_content = db.Column(db.LargeBinary, nullable=False)
