#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session, Flask
from flask_restful import Api, Resource
from datetime import datetime


# Local imports
from config import app, db, api, migrate
# Add your model imports
from models import Customer, Review, Product, OrderedItem


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

api = Api(app)



class AllCustomers(Resource):
     def get(self):
        customers = Customer.query.all()

        response_body = []

        for customer in customers:
            response_body.append(customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number')))

        return make_response(response_body, 200)
    
   
    
     def post(self):
        try:
            new_customer = Customer(email=request.json.get('email'), password=request.json.get('password'), first_name=request.json.get('first_name'), last_name=request.json.get('last_name'), address=request.json.get('address'), phone_number=request.json.get('phone_number'))
            db.session.add(new_customer)
            db.session.commit()
            response_body = new_customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number', 'password'))
            return make_response(response_body, 201)
        except(ValueError):
            response_body = {
                "error": "Invalid value for one or more fields!"
            }
            return make_response(response_body, 422)
    
api.add_resource(AllCustomers, '/customers')



class CustomerById(Resource):
    def get(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number',  'reviews.id', 'reviews.rating', 'ordered_items.id', 'ordered_items.quantity', 'ordered_items.order_date'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Customer Not Found'
            }
            return make_response(response_body, 404)
        
        
        
    def patch(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            for attr in request.json:
                setattr(customer, attr, request.json.get(attr))

            db.session.commit()

            response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number', 'password'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Customer Not Found'
            }
            return make_response(response_body, 404)
        
        # post request is working
    
        
    def delete(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            db.session.delete(customer)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        else:
            response_body = {
                'error': 'Customer Not Found'
            }
            return make_response(response_body, 404)

api.add_resource(CustomerById, '/customers/<int:id>')

class AllProduct(Resource):
    def get(self):
        products = Product.query.all()

        response_body = []

        for product in products:
            response_body.append(product.to_dict(only=('id', 'name', 'price', 'description', 'image_url')))

        return make_response(response_body, 200)
    
    def post(self):
        try:
            new_product = Product(name=request.json.get('name'), price=request.json.get('price'), description=request.json.get('description'), image_url=request.json.get('image_url'), category=request.json.get('category'), stock_quantity=request.json.get('stock_quantity'))
            db.session.add(new_product)
            db.session.commit()
            response_body = new_product.to_dict(only=('id', 'name', 'price', 'description', 'stock_quantity', 'category', 'image_url'))
            return make_response(response_body, 201)
        except(ValueError):
            response_body = {
                "error": "Invalid value for one or more fields!"
            }
            return make_response(response_body, 422)
    
api.add_resource(AllProduct, '/products')



class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id == id).first()

        if product:
            response_body = product.to_dict(only=('id', 'name', 'price', 'description', 'image_url'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Product Not Found'
            }
            return make_response(response_body, 404)
        
        
    def patch(self, id):
        product = Product.query.filter(Product.id == id).first()

        if product:
            for attr in request.json:
                setattr(product, attr, request.json.get(attr))

            db.session.commit()

            response_body = product.to_dict(only=('id', 'name', 'price', 'description', 'image_url'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Product Not Found'
            }
            return make_response(response_body, 404)
        
        
    def delete(self, id):
        product = Product.query.filter(Product.id == id).first()

        if product:
            db.session.delete(product)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        else:
            response_body = {
                'error': 'Product Not Found'
            }
            return make_response(response_body, 404)

api.add_resource(ProductById, '/products/<int:id>')


class ReviewById(Resource):
    def get(self, id):
        review = Review.query.filter(Review.id == id).first()

        if review:
            response_body = review.to_dict(only=('id', 'customer_id', 'product_id', 'rating', 'comment'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Review Not Found'
            }
            return make_response(response_body, 404)
        
    
        
    def patch(self, id):
        review = Review.query.filter(Review.id == id).first()

        if review:
            for attr in request.json:
                setattr(review, attr, request.json.get(attr))

            db.session.commit()

            response_body = review.to_dict(only=('id', 'customer_id', 'product_id', 'rating', 'comment'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Review Not Found'
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        review = Review.query.filter(Review.id == id).first()

        if review:
            db.session.delete(review)
            db.session.commit()
            
            response_body = {}
            return make_response(response_body, 204)
        
        else:
            response_body = {
                'error': 'Review Not Found'
            }
            return make_response(response_body, 404)
api.add_resource(ReviewById, '/reviews/<int:id>')

class OrderedItems(Resource):
    def get(self):
        ordered_items = OrderedItem.query.all()
        response_body = [ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id' )) for ordered_item in ordered_items]
        return make_response(response_body, 200)
    
    def post(self):
        # date_string = "2023-08-04"
        date_string = request.json.get('order_date')
        format_string = "%Y-%m-%d"
        date_time = datetime.strptime(date_string, format_string)
        ordered_item = OrderedItem(
            quantity=request.json.get('quantity'),
            order_date=date_time,
            customer_id=request.json.get('customer_id'),
            product_id=request.json.get('product_id')
        )
        db.session.add(ordered_item)
        db.session.commit()
        response_body = ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id'))
        return make_response(response_body, 201)
    
    
    
api.add_resource(OrderedItems, '/ordered_items')

class OrderedItemsByID(Resource):
    def get(self, id):
        ordered_item = OrderedItem.query.filter(OrderedItem.id == id).first()

        if ordered_item:
            response_body = ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Ordered Item Not Found'
            }
            return make_response(response_body, 404)
    
    def patch(self, id):
        ordered_item = OrderedItem.query.filter(OrderedItem.id == id).first()

        if ordered_item:
            for attr in request.json:
                setattr(ordered_item, attr, request.json.get(attr))

            db.session.commit()

            response_body = ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Ordered Item Not Found'
            }
            return make_response(response_body, 404)
        
    def delete(self, id):
        ordered_item = OrderedItem.query.filter(OrderedItem.id == id).first()

        if ordered_item:
            db.session.delete(ordered_item)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        else:
            response_body = {
                'error': 'Ordered Item Not Found'
            }
            return make_response(response_body, 404)
        
    
        
api.add_resource(OrderedItemsByID, '/ordered_items/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

