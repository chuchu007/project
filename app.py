from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/heimdall.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models_db import db, User
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.before_first_request
def create_tables():
    db.create_all()
