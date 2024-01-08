#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session, Flask
from flask_restful import Api, Resource


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
    
    #get request seems to be working

    def get(self):
        customers = Customer.query.all()

        response_body = []

        for customer in customers:
            response_body.append(customer.to_dict(only=('id', 'username', 'email', 'full_name', 'address', 'phone_number', 'password')))

        return make_response(response_body, 200)
    
    def delete(self):
        pass
    #cant get my post to work
    def post(self):
        try:
            new_customer = Customer(username=request.json.get('username'), email=request.json.get('email'), password=request.json.get('password'), full_name=request.json.get('full_name'), address=request.json.get('address'), phone_number=request.json.get('phone_number'))
            db.session.add(new_customer)
            db.session.commit()
            response_body = new_customer.to_dict(only=('id', 'username', 'email', 'full_name', 'address', 'phone_number', 'password'))
            return make_response(response_body, 201)
        except(ValueError):
            response_body = {
                "error": "Invalid value for hotel!"
            }
            return make_response(response_body, 422)
    
    
    
    
api.add_resource(AllCustomers, '/customers')

class CustomerById(Resource):
    
# get request works for getting all customers
    def get(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            response_body = customer.to_dict(only=('id', 'username', 'email', 'full_name', 'address', 'phone_number', 'password', 'reviews', 'ordered_items'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Customer Not Found'
            }
            return make_response(response_body, 404)
        
        #patch request seems to be working
    def patch(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            for attr in request.json:
                setattr(customer, attr, request.json.get(attr))

            db.session.commit()

            response_body = customer.to_dict(only=('id', 'username', 'email', 'full_name', 'address', 'phone_number', 'password'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Customer Not Found'
            }
            return make_response(response_body, 404)
        
        # post request is working
    def post(self, id):
        try:
            customer = Customer.query.filter(Customer.id == id).first()

            if customer:
                response_body = customer.to_dict(only=('id', 'username', 'email', 'full_name', 'address', 'phone_number', 'password'))
                return make_response(response_body, 200)
            else:
                response_body = {
                    'error': 'Customer Not Found'
                }
                return make_response(response_body, 404)
        except(ValueError):
            response_body = {
                "error": "Invalid value for hotel!"
            }
            return make_response(response_body, 422)
        
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

# class AllProduct(Resource):
#     def get(self):
#         products = Product.query.all()

#         response_body = []

#         for product in products:
#             response_body.append(product.to_dict(only=('id', 'name', 'price', 'description', 'image')))

#         return make_response(response_body, 200)
    
# api.add_resource(AllProduct, '/products')

class ProductById(Resource):
    
# get request works for getting all customers
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
        
        #patch request seems to be working
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
        
        # post request is working
    def post(self, id):
        try:
            product = Product.query.filter(Product.id == id).first()

            if product:
                response_body = product.to_dict(only=('id', 'name', 'price', 'description', 'image_url'))
                return make_response(response_body, 200)
            else:
                response_body = {
                    'error': 'Product Not Found'
                }
                return make_response(response_body, 404)
        except(ValueError):
            response_body = {
                "error": "Invalid value for product!"
            }
            return make_response(response_body, 422)
        # delete request works
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
    # get request works
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
        
    # post request works
    def post(self, id):
        try:
            review = Review.query.filter(Review.id == id).first()

            if review:
                response_body = review.to_dict(only=('id', 'customer_id', 'product_id', 'rating', 'comment'))
                return make_response(response_body, 200)
            else:
                response_body = {
                    'error': 'Review Not Found'
                }
                return make_response(response_body, 404)
        except(ValueError):
            response_body = {
                "error": "Invalid value for review!"
            }
            return make_response(response_body, 422)
        
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
        
api.add_resource(ReviewById, '/reviews/<int:id>')

class OrderedItems(Resource):
    def get(self):
        ordered_items = OrderedItem.query.all()
        response_body = [ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id')) for ordered_item in ordered_items]
        return make_response(response_body, 200)
    
    def post(self):
        ordered_item = OrderedItem(
            quantity=request.json.get('quantity'),
            order_date=request.json.get('order_date'),
            customer_id=request.json.get('customer_id'),
            product_id=request.json.get('product_id')
        )
        db.session.add(ordered_item)
        db.session.commit()
        response_body = ordered_item.to_dict(only=('id', 'quantity', 'order_date', 'customer_id', 'product_id'))
        return make_response(response_body, 201)
    
    def delete(self):
        ordered_item = OrderedItem.query.filter(OrderedItem.id == request.json.get('id')).first()
        
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

