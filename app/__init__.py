from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_cors import CORS

login = LoginManager()
login.login_view = 'auth.login'
login.login_message = "Please login to view this page"
login.login_message_category = "warning"

db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    cors.init_app(app)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # from .blueprints.products_db import bp as productdb_bp
    # app.register_blueprint(productdb_bp)

    # from .blueprints.cart import bp as cart_bp
    # app.register_blueprint(cart_bp)

    from .blueprints.product import bp as product_bp
    app.register_blueprint(product_bp)
    
    return app