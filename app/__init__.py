from flask import Flask
from config import Config
from .models import db, User, Manga

app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()
# Import routes
from . import routes

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
