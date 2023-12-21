from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from services.users_service import create_user, get_user_by_Username, verify_user_password, change_user_password
from utils.auth import get_current_user
from database.db import get_db

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

@router.put("/users/change-password", status_code=status.HTTP_204_NO_CONTENT)
def change_password(
    current_password: str,
    new_password: str,
    confirm_new_password: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
    ):

    if new_password != confirm_new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password and confirmation do not match"
        )

    if not verify_user_password(current_password, current_user.Password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect current password"
        )

    change_user_password(db, current_user.UserID, new_password)

    return None
