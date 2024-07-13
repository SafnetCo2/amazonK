from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.confiq import Config
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        #import routes and models
        from app import models, routes
        db.create_all()
        return app