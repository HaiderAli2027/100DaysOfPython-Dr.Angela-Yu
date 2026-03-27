from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True)
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

# Init Schema 
Product_schema = ProductSchema()
Products_schema = ProductSchema(many=True)

# add product
@app.route("/product", methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    
    db.session.add(new_product)
    db.session.commit()

    return Product_schema.jsonify(new_product)

# Get all Products
@app.route("/product", methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = Products_schema.dump(all_products)
    return jsonify(result)

# Get single Products
@app.route("/product/<id>", methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return Product_schema.jsonify(product)

# Delete Products
@app.route("/product/<id>", methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    
    return Product_schema.jsonify(product)

# Update product
@app.route("/product/<id>", methods=['PUT'])
def update_product(id):

    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return Product_schema.jsonify(product)
# Run Server
if __name__ == '__main__':
    app.run(debug=True)
