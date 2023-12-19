from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "Products"

    ProductID = Column(Integer, primary_key=True, index=True)
    Productname = Column(String, index=True)
    Price = Column(Numeric(precision=10, scale=2))
    