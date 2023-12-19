from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from services.product_service import create_product, get_product_by_Productname
from models.product import Product
from bd import get_db

router = APIRouter()

@router.post("/products/add_product", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = get_product_by_Productname(db, Productname=Product.Productname)
    if db_product:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product already exist")
    return create_product(db, product)
