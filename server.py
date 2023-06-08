from flask import Flask,request

from controllers.dishes import DishAll,DishOne,DishFilter
from controllers.categories import CategoryAll,CategoryOne
from flask_restful import Api
from flask_cors import CORS
from db import db
from config import DBUSER,DBPASS,DBHOST

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = "rggnrkbn454mgfje3"
CORS(app)
db.init_app(app)
api = Api(app)

with app.app_context():
  db.create_all()

api.add_resource(DishAll,'/dishes')
api.add_resource(DishOne,'/dishes/<int:id>')
api.add_resource(CategoryAll,'/categories')
api.add_resource(CategoryOne,'/categories/<int:id>')

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0")
