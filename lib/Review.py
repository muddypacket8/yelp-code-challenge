from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    rating = Column(Integer)

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')
