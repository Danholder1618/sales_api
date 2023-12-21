from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt 
from services import users_service
from database.db import get_db
from models.user import User
from main import oauth2_scheme
from sqlalchemy.orm import Session
from decouple import config

JWT_TOKEN = config('JWT_TOKEN')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_TOKEN, algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    db_user = users_service.get_user_by_username(db, username)
    if db_user is None:
        raise credentials_exception
    return db_user