from sqlalchemy.orm import Session
from models.user_cart import UserCart
from models.user import User

def add_to_cart(db: Session, cart_item: UserCart, current_user: User):
    # Проверка, существует ли уже продукт в корзине пользователя
    existing_cart_item = db.query(UserCart).filter(
        UserCart.UserID == current_user.UserID,
        UserCart.ProductID == cart_item.ProductID
    ).first()

    if existing_cart_item:
        # Если продукт уже в корзине, увеличиваем количество
        existing_cart_item.Quantity += 1
        db.commit()
        db.refresh(existing_cart_item)
        return existing_cart_item
    else:
        # Если продукта нет в корзине, добавляем новый
        db_cart_item = UserCart(
            UserID=current_user.UserID,
            ProductID=cart_item.ProductID,
            Quantity=1
        )
        db.add(db_cart_item)
        db.commit()
        db.refresh(db_cart_item)
        return db_cart_item
 
def remove_from_cart(db: Session, cart_item: UserCart, current_user: User):
    # Проверка, существует ли продукт в корзине пользователя
    existing_cart_item = db.query(UserCart).filter(
        UserCart.UserID == current_user.UserID,
        UserCart.ProductID == cart_item.ProductID
    ).first()

    if existing_cart_item:
        # Если продукт в корзине, уменьшаем количество
        existing_cart_item.Quantity -= 1

        # Если количество стало равным нулю, удаляем запись из корзины
        if existing_cart_item.Quantity <= 0:
            db.delete(existing_cart_item)
        else:
            db.commit()
            db.refresh(existing_cart_item)

        return existing_cart_item
    else:
        return None

def get_user_cart(db: Session, user_id: int):
    return db.query(UserCart).filter(UserCart.UserID == user_id).all()
