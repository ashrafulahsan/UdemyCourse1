from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay, UserBase
from auth.oauth2 import oauth2_scheme, get_current_user, create_access_token    

router = APIRouter(
    prefix="/article",
    tags=["article"]
)  

# Create Article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Get Article by ID
@router.get("/{id}")
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    article = db_article.get_article(db, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return {
        "article": article,
        "current_user": current_user
    }