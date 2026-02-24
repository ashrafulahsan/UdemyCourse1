from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from auth.oauth2 import oauth2_scheme

router = APIRouter(
    prefix="/article",
    tags=["article"]
)  

# Create Article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

# Get Article by ID
@router.get("/{id}", response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    article = db_article.get_article(db, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article