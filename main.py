from fastapi import FastAPI
from db.database import engine
from router import user
from router import article
from router import blog
from db import models

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello World"}
