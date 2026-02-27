from fastapi import APIRouter, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemas import ProductBase
from custom_log import log

router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

templates = Jinja2Templates(directory="templates")

@router.post("/products/{id}", response_class=HTMLResponse)
def get_product_template(id: int, product: ProductBase, request: Request, bt: BackgroundTasks):         
    bt.add_task(log_template_call, f"Product template called for product id: {id}")
    return templates.TemplateResponse(
        "product.html", 
        {
            "request": request, 
            "id": id,
            "name": product.name,
            "description": product.description,
            "price": product.price
        }
    )

def log_template_call(message: str):
    log('Info', message)