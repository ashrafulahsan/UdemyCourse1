import time
from fastapi import FastAPI, WebSocket
from db.database import engine
from router import user, article, blog, product, file
from auth import authentication
from db import models
from exceptions import StoryException
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from templates import templates
from client import html


app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog.router)
app.include_router(product.router)
app.include_router(file.router)

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )

models.Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def greet():
    return HTMLResponse(html)

clients = []

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)

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

app.mount("/files", StaticFiles(directory="files"), name="files")

app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")