from flask import Flask
from flask_cors import CORS
from config import Config
from flask_jwt_extended import JWTManager
from models import db
from routers.api import api
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)
JWTManager(app)

db.init_app(app)
app.register_blueprint(api, url_prefix='/api')
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)