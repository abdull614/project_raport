from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
import os
load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))
app.config.from_object(config)

db= SQLAlchemy(app)
migrate=Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

app.jinja_env.globals.update(enumerate=enumerate)

from app.model import user, guru, kelas, siswa, mataPelajaran, nilai, laporan, admin
from app import routes

from app.model.admin import Admin
@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))