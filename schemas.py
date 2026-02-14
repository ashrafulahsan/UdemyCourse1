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


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    author_id: int

#User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class Config():
        from_attributes = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        from_attributes = True