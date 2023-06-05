from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Customer import Customer
from Restaurant import Restaurant
from Review import Review
import ipdb

# Create an engine and create the tables
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample usage
customer1 = Customer(given_name="Collins, family_name="Kimani")
customer2 = Customer(given_name="Cole", family_name="Mburu")
restaurant = Restaurant(name="La`peri")

review1 = Review(customer=customer1, restaurant=restaurant, rating=5)
review2 = Review(customer=customer2, restaurant=restaurant, rating=4)

session.add_all([customer1, customer2, restaurant, review1, review2])
session.commit()

print(restaurant.average_star_rating())  
print(restaurant.customers())  


ipdb.set_trace()
