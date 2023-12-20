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

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.ProductID == product_id).first()

def delete_product(db: Session, db_product: Product):
    db.delete(db_product)
    db.commit()
    return db_product
