from flask import request
from flask_restful import Resource
from db import db
from models.category import Category

class CategoryAll(Resource):
  def get(self):
    categories = Category.query.all()
    return [category.serialize() for category in categories]
  def post(self):
    data = request.get_json()
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return {'message':f'{category.name} was added!'}, 201

class CategoryOne(Resource):
  def get(self,id):
    category = Category.query.get(id)
    return category.serialize()
  def delete(self,id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return {'message':'category was deleted!'}
