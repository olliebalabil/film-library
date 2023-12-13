from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wumfxrod:1LRvnB-2v36E81EwsDLpXq6_YkYId_c5@flora.db.elephantsql.com/wumfxrod'
db = SQLAlchemy(app)

from application import routes