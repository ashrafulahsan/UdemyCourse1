from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from schemas import ProductBase

router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/products/{id}", response_class=HTMLResponse)
def get_product_template(id: int, product: ProductBase, request: Request):         
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
