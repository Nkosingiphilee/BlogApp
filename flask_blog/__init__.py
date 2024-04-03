import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = '2020325555825'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] ='phungulankosingiphile828@gmail.com'#os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] ='Kwandiso'#os.environ.get('MAIL_PASSWORD')
mail = Mail(app)
moment=Moment(app)

from flask_blog import routes