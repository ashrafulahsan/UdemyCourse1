from fastapi import FastAPI
from router import blog

app = FastAPI()
app.include_router(blog.router)

@app.get("/")
def greet():
    return {"message": "Hello World"}





