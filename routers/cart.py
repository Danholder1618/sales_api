from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user_cart import UserCart
from models.product import Product
from models.user import User
from services.user_service import get_current_user
from services.user_cart_service import add_to_cart, get_user_cart
from typing import List
from bd import get_db

router = APIRouter()

@router.post("/user-cart/add-to-cart", response_model=UserCart, status_code=status.HTTP_201_CREATED)
def add_to_user_cart(
        cart_item: UserCart,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
    ):
    # Проверка на существование товара
    if not db.query(Product).filter(Product.ProductID == cart_item.ProductID).first():
        raise ValueError("Товар с указанным ProductID не найден на полке продаж.")

    return add_to_cart(db, cart_item, current_user)

@router.get("/user-cart/get_cart_contents", response_model=List[UserCart])
def get_cart_contents(user_id: int, db: Session = Depends(get_db)):
    return get_user_cart(db, user_id)
