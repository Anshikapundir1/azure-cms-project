"""
The flask application package.
"""
import logging
import sys
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# TODO: Add any logging levels and handlers with app.logger
# Configure logging for Azure
if not app.debug:
    # In production (Azure), log to stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    
    # Log application startup
    app.logger.info('=' * 50)
    app.logger.info('Article CMS starting up in production mode')
    app.logger.info('=' * 50)
else:
    # In development, more verbose logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
    app.logger.debug('Article CMS starting up in debug mode')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Import views and models at the end to avoid circular imports
import FlaskWebProject.views
import FlaskWebProject.models

