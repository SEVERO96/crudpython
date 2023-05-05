from flask import Flask,Blueprint,request, jsonify, make_response
from response.generic_response import Responses
from db import db

article_bp = Blueprint('article', __name__, url_prefix="/articles")

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    
 
    def json(self):
        return {'id': self.id,'name': self.name, 'description': self.description}


# create a article
@article_bp.post("")
def create_article():
  try:
    data = request.get_json()
    new_article = Article(name=data['name'], description=data['description'])
    db.session.add(new_article)
    db.session.commit()
    return make_response(jsonify({'message': 'article created'}), 201)
  except:
    return make_response(jsonify({'message': 'error creating article'}), 500)

# get all articles
@article_bp.get("")
def get_articles():
  try:
    articles = Article.query.all()
    return make_response(jsonify([article.json() for article in articles]), 200)
  except:
    return make_response(jsonify({'message': 'error getting articles'}), 500)

# get a article by id
@article_bp.get("/<int:id>")
def get_article(id):
  try:
    article = Article.query.filter_by(id=id).first()
    if article:
      return make_response(jsonify({'article': article.json()}), 200)
    return make_response(jsonify({'message': 'article not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error getting article'}), 500)

# update a article
@article_bp.put("/<int:id>")
def update_article(id):
  try:
    article = Article.query.filter_by(id=id).first()
    if article:
      data = request.get_json()
      article.name = data['name']
      article.description = data['description']
      db.session.commit()
      return make_response(jsonify({'message': 'article updated'}), 200)
    return make_response(jsonify({'message': 'article not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error updating article'}), 500)

# delete a article
@article_bp.delete("/<int:id>")
def delete_article(id):
  try:
    article = Article.query.filter_by(id=id).first()
    if article:
      db.session.delete(article)
      db.session.commit()
      return make_response(jsonify({'message': 'article deleted'}), 200)
    return make_response(jsonify({'message': 'article not found'}), 404)
  except:
    return make_response(jsonify({'message': 'error deleting article'}), 500)