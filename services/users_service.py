from sqlalchemy.orm import Session
from models.user import User

def get_user_by_Username(db: Session, Username: str):
    return db.query(User).filter(User.Username == Username).first()

def create_user(db: Session, username: str, password: str):
    db_user = User(Username=username, Password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
