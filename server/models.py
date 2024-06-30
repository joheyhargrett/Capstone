from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
import re


from config import db, bcrypt

# Models go here!
class Admin(db.Model, SerializerMixin):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(120), nullable=False, unique=True)
    _password_hash = db.Column(db.String(255))

    serialize_rules = ('-_password_hash',)

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    @validates('username')
    def validate_username(self, key, username):
        if not (len(username) > 1 and len(username) <= 120 and ' ' not in username):
            raise ValueError('Invalid username')
        return username

    def __repr__(self):
        return f"<Admin {self.id} {self.name} {self.username}>"

class Customer(db.Model, SerializerMixin):
    __tablename__ = "customers"
    
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    _password_hash = db.Column(db.String(255))
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)

    reviews = db.relationship('Review', back_populates="customer", cascade="all, delete-orphan")
    ordered_items = db.relationship('OrderedItem', back_populates='customer', cascade='all, delete-orphan')
    
    
    
    serialize_rules =('-_password_hash',)
    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed')
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    def authenticate(self, password):
        return bcrypt.check_password_hash(
        self._password_hash, password.encode('utf-8'))
    
        
    @validates('email')
    def validate_email(self, key, email):
        if not ('@' in email and '.' in email and len(email) > 1 and len(email) <= 120 and ' ' not in email):
            raise ValueError('Invalid email')
        return email
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        #Phone number validation: allowing digits, spaces, hyphens, and parentheses
        if not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise ValueError('Invalid phone number')
        return phone_number
    
    @validates('first_name', 'last_name')
    def validate_name(self, key, name):
        if not name.isalpha() or len(name) < 1 or len(name) > 100:
            raise ValueError(f'Invalid {key}')
        return name

    @validates('address')
    def validate_address(self, key, address):
        if len(address) < 1 or len(address) > 255:
            raise ValueError('Invalid address')
        return address
    

    def __repr__(self):
        return f"<Customer {self.id} {self.first_name} {self.last_name} {self.email}  {self.address} {self.phone_number} >"



class Product(db.Model, SerializerMixin):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    
    ordered_items = db.relationship('OrderedItem', back_populates='product', cascade='all, delete-orphan')
    
    reviews = db.relationship('Review', back_populates="product", cascade="all, delete-orphan")
    
    
    
    def __repr__(self):
        return f"<Product {self.id} {self.name} {self.description} {self.price} {self.stock_quantity} {self.category} {self.image_url}>"



class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"
    
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product = db.relationship('Product', back_populates="reviews")
    customer = db.relationship('Customer', back_populates="reviews")
    
    @validates('rating')
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError('Rating must have a rating between 1 and 5')
        return rating


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
        return f"<OrderItem {self.id} {self.quantity} {self.order_date}>"
