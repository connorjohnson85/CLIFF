from flask import Flask, render_template
from app.config import Config
from app.forms import LoginForm
from flask import flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = b'asft323hgfs?d&fd@#'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models