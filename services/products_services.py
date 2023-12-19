from sqlalchemy.orm import Session
from models.product import Product

def get_product_by_Productname(db: Session, Productname: str):
    return db.query(Product).filter(Product.Productname == Productname).first()

def create_product(db: Session, productname: str, price: str):
    db_product = Product(Productname=productname, Price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
