#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session
from flask_restful import Api, Resource
from datetime import datetime


# Local imports
from config import app, db, api, migrate, bcrypt
# Add your model imports
from models import Customer, Review, Product, OrderedItem



# Views go here!

# My root endpoint
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

api = Api(app)




# Resource for handling requests for all customers
class AllCustomers(Resource):
    # GET request to get all customers
    def get(self):
        # Querying all customers from the database
        customers = Customer.query.all()

        response_body = []
        # Getting customers from the database and adding them to the response body
        for customer in customers:
            response_body.append(customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number')))

        return make_response(response_body, 200)
    
    
     
        
# Adding the AllCustomers resource to the API with a route of /customers  
api.add_resource(AllCustomers, '/customers')

# Resource for handling login requests
class Login(Resource):
    def post(self):
        
        customer_email = request.json.get('email')
        customer_password = request.json.get('password')
        
        # Querying the customer with the given email from the database
        customer = Customer.query.filter_by(email=customer_email).first()
        
        if customer and customer.authenticate(customer_password):
            # Setting the customer id in the session if the password is correct
         
            session['customer_id'] = customer.id
            
            response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number'))
            
            return make_response(response_body, 201) 
        else:
            response_body = {
                'error': 'Login Failed',
                'details': 'Invalid email or password'}
        return make_response(response_body, 401)
    
    # Adding the Login resource to the API with a route of /login
api.add_resource(Login, '/login')


# Resource for checking the session and retrieving the customer details
class CheckSession(Resource):
    def get(self):
        # Retrieving the customer ID from the session
        customer_id = session.get('customer_id')
       
        print(customer_id)
        if customer_id:
            # Querying the customer with the customer ID from the session

            customer = Customer.query.filter(Customer.id == customer_id).first()
            
            print(customer)
            if customer:
                # Prepare response body with detailed customer information
                response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number'))
                return make_response(response_body, 200)
            
        # If no customer is logged in, return an error response
        response_body = {
            'error': 'Please log into your account',
            'details': 'No user logged in'}
        return make_response(response_body, 401)
    

# Add the '/check_session' endpoint to the API with the CheckSession resource
api.add_resource(CheckSession, '/check_session')


class Logout(Resource):
    def delete(self):
        if session.get('customer_id'):
            session['customer_id'] = None 
            session.pop('customer_id', None)
            response = make_response({"message": "Logged out successfully"}, 200)
            response.set_cookie('id', '', expires=0, path='/', httponly=True)  # Clear the 'id' cookie
            return response
        return make_response({'error': 'Unauthorized'}, 401)
    
api.add_resource(Logout, '/logout')
 
        



class SignUp(Resource):
    def post(self):
        # Creating and adding new customer in the database
        customer_email = request.json.get('email')
        customer_password = request.json.get('password')
        customer_first_name = request.json.get('first_name')
        customer_last_name = request.json.get('last_name')
        customer_address = request.json.get('address')
        customer_phone_number = request.json.get('phone_number')
        
        # Hashing the password before adding it to the database
        
        # Creating and adding new customer in the database
        new_customer = Customer(first_name = customer_first_name, last_name = customer_last_name, 
                                email = customer_email, address = customer_address, phone_number = customer_phone_number)
        new_customer.password_hash = customer_password
        # Adding new customer to the database
        db.session.add(new_customer)
        db.session.commit()

        # Setting the customer id in the session
        session['customer_id'] = new_customer.id
        
        # Prepare response body with detailed customer information
        response_body = new_customer.to_dict(
            only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number')
            )
        
        return make_response(response_body, 201)
 # Add the '/signup' endpoint to the API with the SignUp resource   
api.add_resource(SignUp, '/signup')



# My Resource for handling requests for a specific customer by ID
class CustomerById(Resource):
    def get(self, id):
        
        # Retrieving the customer with the specified ID from the database
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            # Prepare response body with detailed customer information
            response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number',  'reviews.id', 'reviews.rating', 'ordered_items.id', 'ordered_items.quantity', 'ordered_items.order_date'))
            
            return make_response(response_body, 200)
        else:
            # Handle customer not found
            response_body = {
                'error': 'Customer Not Found',
                'details': f'Customer with ID {id} does not exist.'
            }
            return make_response(response_body, 404)
        
        
        
    def patch(self, id):
        # Updating the customer with the specified ID in the database
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            # Update the customer attributes with the new values from the request
            for attr in request.json:
                setattr(customer, attr, request.json.get(attr))

            db.session.commit()

            response_body = customer.to_dict(only=('id', 'email', 'first_name', 'last_name', 'address', 'phone_number'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Customer Not Found',
                'details': f'Customer with ID {id} does not exist.'
            }
            return make_response(response_body, 404)
        
        
    
        
    def delete(self, id):
        customer = Customer.query.filter(Customer.id == id).first()

        if customer:
            db.session.delete(customer)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        else:
            response_body = {
                'error': 'Customer Not Found',
                'details': f'Customer with ID {id} does not exist.'
            }
            return make_response(response_body, 404)
        
    

api.add_resource(CustomerById, '/customers/<int:id>')

# Need to finish code to add admin features

# class SetAdmin(Resource):
#     @admin_required  # Ensure this is a decorator that checks if the user is an admin
#     def patch(self, user_id):
#         user = Customer.query.get(user_id)
#         if not user:
#             return {'message': 'User not found'}, 404
        
#         user.role = 'admin'
#         db.session.commit()
#         return {'message': f'User {user_id} set as admin'}, 200

# api.add_resource(SetAdmin, '/set-admin/<int:user_id>')


class AllProduct(Resource):
    def get(self):
        products = Product.query.all()

        response_body = []

        for product in products:
            response_body.append(product.to_dict(only=('id', 'name', 'price', 'description', 'image_url', 'category', 'stock_quantity')))

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
                "error": "Invalid value for one or more fields!",
                "details": "The following fields are required: name, price, description, image_url, category, stock_quantity"
            }
            return make_response(response_body, 422)
    
api.add_resource(AllProduct, '/products')



class ProductById(Resource):
    def get(self, id):
        product = Product.query.filter(Product.id == id).first()

        if product:
            response_body = product.to_dict(only=('id', 'name', 'price', 'description', 'image_url', 'category', 'stock_quantity', 'reviews.rating'))
            return make_response(response_body, 200)
        else:
            response_body = {
                'error': 'Product Not Found',
                'details': f'Product with ID {id} does not exist.'
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
                'error': 'Product Not Found',
                'details': f'Product with ID {id} does not exist.'
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
                'error': 'Product Not Found',
                'details': f'Product with ID {id} does not exist.'  
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
                'error': 'Review Not Found',
                'details': f'Review with ID {id} does not exist.'
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
                'error': 'Review Not Found',
                'details': f'Review with ID {id} does not exist.'
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
                'error': 'Review Not Found',
                'details': f'Review with ID {id} does not exist.'
            }
            return make_response(response_body, 404)
api.add_resource(ReviewById, '/reviews/<int:id>')



# class AverageRating(Resource):
    
#     def get(self, product_id):
#         reviews = Review.query.filter(Review.product_id == product_id).all()
#         ratings = [review.rating for review in reviews]
#         average_rating = sum(ratings) / len(ratings)
#         response_body = {'average_rating': average_rating}
#         return make_response(response_body, 200)


# api.add_resource(AverageRating, '/reviews/average_rating/<int:product_id>')

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
                'error': 'Ordered Item Not Found',
                'details': f'Ordered Item with ID {id} does not exist.'
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
                'error': 'Ordered Item Not Found',
                'details': f'Ordered Item with ID {id} does not exist.'
            }
            return make_response(response_body, 404)
        
    
        
    
        
api.add_resource(OrderedItemsByID, '/ordered_items/<int:id>')




if __name__ == '__main__':
    app.run(port=5555, debug=True)

