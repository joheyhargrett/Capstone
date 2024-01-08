from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from datetime import datetime

from config import db

# Models go here!
class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"
    
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)

    reviews = db.relationship('Review', back_populates="customer", cascade="all, delete-orphan")
    ordered_items = db.relationship('OrderedItem', back_populates='customer', cascade='all, delete-orphan')
    
    

    def __repr__(self):
        return f"<Customer {self.id} {self.username} {self.email} {self.full_name} {self.address} {self.phone_number}>"



class Product(db.Model, SerializerMixin):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    
    ordered_items = db.relationship('OrderedItem', back_populates='product', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Product {self.id} {self.name} {self.description} {self.price} {self.stock_quantity} {self.category} {self.image_url}>"



class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
   
    customer = db.relationship('Customer', back_populates="reviews")
    
    @validates('rating')
    def validate_rating(self, key, value):
        if not (0 <= value <= 5):
            raise ValueError('Rating must have a rating between 0 and 5')
        return value


    def __repr__(self):
        return f"<Review {self.id} {self.rating} {self.comment}>"


class OrderedItem(db.Model, SerializerMixin):
    __tablename__ = "ordered_items"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
    customer = db.relationship('Customer', back_populates='ordered_items')
    product = db.relationship('Product', back_populates='ordered_items')
    
    
    def __repr__(self):
        return f"<OrderItem {self.id} {self.quantity}>"
