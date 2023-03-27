from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from views import bp
import os

app = Flask(__name__)

database_uri = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db.init_app(app)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
