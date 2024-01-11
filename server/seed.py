# Standard library imports
from random import randint
from models import Customer, Review, Product, OrderedItem, db
from datetime import datetime

# Remote library imports
from faker import Faker

# Local imports
from app import app
from config import bcrypt

with app.app_context():
    fake = Faker()

    def format_phone_number(raw_phone):
        return f"({raw_phone[0:3]}) {raw_phone[3:6]}-{raw_phone[6:]}"

    ratings_and_comments = [
    (5, "Excellent product, exceeded my expectations!"),
    (4, "Fast shipping and great customer service."),
    (1, "Not as described. Very disappointed."),
    (5, "Highly recommended! Will buy again."),
    (5, "The quality is unmatched. Very satisfied."),
    (2, "Poor packaging, item arrived damaged."),
    (5, "Exactly what I needed. Thank you!"),
    (2, "Product didn't meet my expectations."),
    (4, "Amazing value for the price!"),
    (3, "Item arrived on time, but with minor flaws."),
    (5, "Outstanding quality and craftsmanship."),
    (1, "Terrible experience. Avoid this product."),
    (4, "Prompt delivery and hassle-free return process."),
    (3, "Good product, but a bit overpriced."),
    (5, "Superb customer support. Resolved my issue quickly."),
    (2, "Average product. Nothing special."),
    (4, "Great value for money. Would recommend."),
    (2, "The color doesn't match the picture online."),
    (5, "Perfect fit and excellent build quality."),
    (1, "Disappointing purchase. Won't buy again."),
    (3, "Impressed with the product quality."),
    (4, "Fast and reliable shipping service."),
    (1, "Worst purchase ever. Regret buying."),
    (5, "Absolutely love this product!"),
    (3, "Decent product, but not outstanding."),
    (4, "Good experience overall. Will shop again."),
    (2, "Shipping took longer than expected."),
    (5, "Top-notch customer service."),
    (1, "Misleading product description."),
    (3, "Satisfactory purchase. Could be better."),
    (4, "Well-packaged and arrived in perfect condition."),
    (2, "Product had minor defects."),
    (5, "Exemplary quality and craftsmanship."),
    (1, "Received the wrong item. Very frustrating."),
    (3, "Average product for the price."),
    (4, "Happy with the purchase. Would recommend."),
    (2, "Difficulties with the return process."),
    (5, "Amazing product! Worth every penny."),
    (1, "Never buying from this seller again."),
    (3, "Met my expectations. Nothing extraordinary."),
    (4, "Excellent service and product."),
    (2, "Product broke after a short period."),
    (5, "Absolutely fantastic! No complaints."),
    (1, "Regretting this purchase. Poor quality."),
    (3, "Fair product for the price."),
    (4, "Great value and quality."),
    (2, "Customer service needs improvement."),
    (5, "Thrilled with my purchase!"),
    ]

    Customer.query.delete()
    Product.query.delete()
    Review.query.delete()
    OrderedItem.query.delete()

    customers = []

    for n in range(50):
        raw_phone_number = fake.numerify(text='##########')
        formatted_phone_number = format_phone_number(raw_phone_number)
        
        password = fake.password().encode('utf-8')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        customer = Customer(
            first_name=fake.first_name(), 
            last_name=fake.last_name(),
            email=fake.email(),
            password=hashed_password,
            address=fake.address(),
            phone_number=formatted_phone_number
        )
        customers.append(customer)

    products = []

    for n in range(50):
        product = Product(
            name=fake.word(),
            description=fake.paragraph(),
            price=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
            stock_quantity=randint(1, 100),
            category=fake.word(),
            image_url=fake.image_url()
        )
        products.append(product)

    reviews = []
    ordered_items = []

    for rating, comment in ratings_and_comments:
        ran_customer_id = randint(1, 50)
        ran_product_id = randint(1, 50)

        ordered_item = OrderedItem(
            quantity=randint(1, 5),
            customer_id=ran_customer_id,
            product_id=ran_product_id,
            order_date=fake.date_time_between(
                start_date=datetime(datetime.now().year, 1, 1),
                end_date=datetime.now()
            )
        )

        review = Review(
            rating=rating,
            comment=comment,
            customer_id=ran_customer_id,
            product_id=ran_product_id,
        )

        ordered_items.append(ordered_item)
        reviews.append(review)

    db.session.add_all(customers)
    db.session.add_all(products)
    db.session.add_all(ordered_items)
    db.session.add_all(reviews)
    db.session.commit()

    print("Seed completed.")

