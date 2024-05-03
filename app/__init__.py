from flask import Flask
from .config.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.blueprints.expenses.routes import expenses
    from app.blueprints.users.routes import users

    app.register_blueprint(expenses, url_prefix='/expenses')
    app.register_blueprint(users, url_prefix='/users')

    return app
