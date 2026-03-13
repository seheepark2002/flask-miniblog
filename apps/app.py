from pathlib import Path
from flask import Flask
from apps.crud import views as crud_views
from apps.miniblog import views as miniblog_views
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
    SECRET_KEY="83hfwkfn3SJW3",
    SQLALCHEMY_DATABASE_URI= f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}", SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
    app.config["SECRET_KEY"] = "83hfwkfn3SJW3"

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    app.register_blueprint(miniblog_views.miniblog)

    db.init_app(app)
    Migrate(app, db)

    from apps.models.user import User #모델 import (migration 인식용)

    return app
