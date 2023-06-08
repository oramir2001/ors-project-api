from db import db

class Category(db.Model):
  __tablename__="category"
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(200))
  image = db.Column(db.String(2000))
  dishes = db.relationship('Dish', backref='category')

  def serialize(self):
    return {
      "id":self.id,
      "name":self.name,
      "image":self.image,
      "dishes":[dish.serialize() for dish in self.dishes]
    }

