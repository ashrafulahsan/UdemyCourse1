from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(
    prefix="/products", 
    tags=["products"]
)

products = ["Product 1","Product 2","Product 3"]

@router.get("/all")
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")