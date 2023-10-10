from routers.contacts import contacts
from flask import Flask
from utils.db import db
from config import DATABASE_CONECTION_URI

app = Flask(__name__)


app.secret_key = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.register_blueprint(contacts)
