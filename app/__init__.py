
# app/__init__.py
from os.path import join, dirname
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_heroku import Heroku

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()
heroku = Heroku()


def create_app(config_type):
    # dev, test, prod
    app = Flask(__name__)

    current_dir = dirname(__file__)
    configuration = join(current_dir, ("config\\" + config_type + '.py'))
    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication as at
    app.register_blueprint(at)

    return app
