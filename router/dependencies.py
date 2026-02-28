from fastapi import APIRouter, Depends, Request
from websockets import headers

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"]
)

def convert_headers(request: Request, separetor: str = " --:-- "):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {separetor} {value}")
    return out_headers

@router.get("/headers")
def get_headers(headers: list[str] = Depends(convert_headers)):
    return {
        'item': ['a', 'b', 'c'],
        'headers': headers
    }

@router.get("/products-with-headers")
def get_products_with_headers(headers = Depends(convert_headers)):
    return {
        'item': ['product1', 'product2', 'product3'],
        'headers': headers
    }