from fastapi import FastAPI
from db.database import engine
from router import user, article, blog, product
from auth import authentication
from db import models
from exceptions import StoryException
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog.router)
app.include_router(product.router)

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello World"}


origins = [
    "http://localhost:3000"
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"], # get, post , put, delete
    allow_headers=["*"], # content-type, authorization
    allow_credentials=True,
)