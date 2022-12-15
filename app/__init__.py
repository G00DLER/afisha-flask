from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'anykey'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='Админка', template_mode='bootstrap4')

from app import routes, models
