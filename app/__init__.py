# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_type):
    # dev, test, prod
    app = Flask(__name__)
    app.config.from_pyfile(r'C:\Users\Snick\Documents\Personal_Sync\Personal\python_flask_test\app\config')
    db.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)
    return app
