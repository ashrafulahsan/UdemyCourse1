from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

#Create user
@router.post("/add", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

#Get all users
@router.get("/all", response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

#Get user by ID
@router.get("/{id}", response_model=UserDisplay)   
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, id)

#Update user
@router.put("/update/{id}", response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)

@router.delete("/delete/{id}", response_model=UserDisplay)
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)