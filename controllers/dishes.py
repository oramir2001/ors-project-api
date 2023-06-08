from flask import request
from flask_restful import Resource
from db import db
from models.dish import Dish

class DishAll(Resource):
  def get(self):
    # dishes = Dish.query.filter_by(id=request.args('category_id')).all()
    dishes = Dish.query.all()
    return [dish.serialize() for dish in dishes][::-1]
  def post(self):
    data = request.get_json()
    try:
      dish = Dish(**data)
      db.session.add(dish)
      db.session.commit()
      return {'message':f'{dish.name} was added!'}, 201
    except:
      return {'message':'bad request'},400

class DishOne(Resource):
  def get(self,id):
    dish = Dish.query.get(id)
    return dish.serialize()
  def delete(self,id):
    dish = Dish.query.get(id)
    db.session.delete(dish)
    db.session.commit()
    return {'message':'dish was deleted!'}

class DishFilter(Resource):
  def get(self,category_id):
    dishes = Dish.query.filter_by(category_id=category_id).all()
    return [dish.serialize() for dish in dishes]
