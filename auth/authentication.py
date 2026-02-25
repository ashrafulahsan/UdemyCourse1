from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from db.hash import Hash
from auth import oauth2


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/token")
def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(models.DbUser.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid username")
    if not Hash.verify(user.password, form_data.password):
        raise HTTPException(status_code=404, detail="Invalid password")
    
    access_token = oauth2.create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username
    }


    