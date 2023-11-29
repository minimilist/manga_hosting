import os
import secrets
from urllib.parse import quote

class Config:
    SECRET_KEY = secrets.token_hex(16)
    password = "@Mukherjee2002"
    encoded_password = quote(password)
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{encoded_password}@localhost:5432/manga_hosting'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = secrets.token_urlsafe(32)
