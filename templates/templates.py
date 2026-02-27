from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/products/{id}", response_class=HTMLResponse)
def get_product_template(id: int, request: Request):
    product = {
        "id": id, 
        "name": f"Product {id}", 
        "price": 99.99
    }        
    return templates.TemplateResponse(
        "product.html", 
        {"request": request, "product": product}
    )
