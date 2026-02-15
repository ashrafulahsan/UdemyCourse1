from pydantic import BaseModel
from typing import List

# Article Inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    article: List[Article] = []
    class Config():
        from_attributes = True

#User inside ArticleDisplay
class User(BaseModel):
    username: str
    class Config():
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    author_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    users: List[User] = []
    class Config():
        from_attributes = True