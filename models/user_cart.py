from sqlalchemy import Column, Integer, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserCart(Base):
    __tablename__ = "UserCart"

    CartID = Column(Integer, primary_key=True, index=True)
    UserID= Column(String, index=True)
    ProductID = Column(String, index=True)
    Quantity = Column(Integer)
