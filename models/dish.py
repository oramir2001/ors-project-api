from db import db
from datetime import datetime as dt

class Dish(db.Model):
  __tablename__="dish"
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(200))
  price = db.Column(db.Integer, nullable = False)
  description = db.Column(db.String(2000))
  image = db.Column(db.String(2000))
  is_gluten_free = db.Column(db.Boolean)
  is_vageterian = db.Column(db.Boolean)
  category_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

  def serialize(self):
    return {
      "id":self.id,
      "name":self.name,
      "price":self.price,
      "description":self.description,
      "image":self.image,
      "is_gluten_free":self.is_gluten_free,
      "is_vageterian":self.is_vageterian,
      "category_id": self.category_id
    }
