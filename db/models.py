from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db.database import Base

class DbUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    article = relationship("DbArticle", back_populates="user")

class DbArticle(Base):
    __tablename__ = "articles" 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="article")