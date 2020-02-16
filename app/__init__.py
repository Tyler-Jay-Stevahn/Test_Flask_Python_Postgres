# app/__init__.py

from os.path import dirname, join
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_type):
    # dev, test, prod
    app = Flask(__name__)

    current_dir = dirname(__file__)
    configuration = join(current_dir, ("config\\" + config_type + '.py'))
    app.config.from_pyfile(configuration)
    db.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    return app
