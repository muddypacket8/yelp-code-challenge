from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    reviews = relationship('Review', back_populates='restaurant')

    def average_star_rating(self):
        if not self.reviews:
            return 0

        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    def customers(self):
        return list(set([review.customer for review in self.reviews]))
