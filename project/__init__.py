from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'cdccefb9e9b1f59ecbb3d6e3653ac636'
    app.config['SQLaLCHEMY_DATABASE_URI'] = "sqlite///site.db"
    db.init_app(app)

    # from .models import User
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

