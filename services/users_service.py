from sqlalchemy.orm import Session
from models.user import User
from security import hash_password

def get_user_by_Username(db: Session, Username: str):
    return db.query(User).filter(User.Username == Username).first()

def create_user(db: Session, username: str, password: str):
    db_user = User(Username=username, Password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_user_password(plain_password: str, hashed_password: str) -> bool:
    return hash_password.verify(plain_password, hashed_password)

def change_user_password(db: Session, user_id: int, new_password: str):
    hashed_password = hash_password(new_password)
    db.query(User).filter(User.UserID == user_id).update({"Password": hashed_password})
    db.commit()
