import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as user_router
from routers.products import router as product_router
from routers.user_carts import router as cart_router
from utils.auth import get_current_user
from database.db import get_db, Session

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7500)
