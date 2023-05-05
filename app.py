from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from db import db
from models.user_model import user_bp
from models.article_model import article_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

app.register_blueprint(article_bp)
app.register_blueprint(user_bp)

db.init_app(app)
with app.app_context():
  db.create_all()
  
@app.route('/')
def index():
    return 'API Created by: Severo Iglesiaaas!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)