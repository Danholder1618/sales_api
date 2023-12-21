from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_user_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_Username(db: Session, Username: str):
    return db.query(User).filter(User.Username == Username).first()

def create_user(db: Session, username: str, password: str, email: str):
    hashed_password = get_password_hash(password)
    db_user = User(Username=username, Password=hashed_password, Email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def change_user_password(db: Session, user_id: int, new_password: str):
    hashed_password = get_password_hash(new_password)
    db.query(User).filter(User.UserID == user_id).update({"Password": hashed_password})
    db.commit()
