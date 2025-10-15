from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager
from models import db

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)
JWTManager(app)

db.init_app(app)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)