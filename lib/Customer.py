from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
