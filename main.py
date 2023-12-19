import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.product import Product
from models.order import Order
from routers import user, product, order
from services import user_service, product_service, order_service
from utils.auth import get_current_user

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация роутеров
app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)

# Регистрация зависимости для получения текущего пользователя
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7500)