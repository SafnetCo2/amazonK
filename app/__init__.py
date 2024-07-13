import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Verify that the DATABASE_URL is being read correctly
    print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app import models, routes
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    print("Starting Flask app...")
    app.run(port=5000, debug=True)
