from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from services.user_service import create_user, get_user_by_Username
from utils.auth import get_current_user
from bd import get_db

router = APIRouter()

@router.post("/users/create_new_user", response_model=User, status_code=status.HTTP_201_CREATED)
def create_new_user(user: User, db: Session = Depends(get_db)):
    db_user = get_user_by_Username(db, Username=User.Username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    return create_user(db, user)

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
