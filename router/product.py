from fastapi import APIRouter, Cookie, Form, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List
from custom_log import log
import time

router = APIRouter(
    prefix="/products", 
    tags=["products"]
)

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 499.99},
    {"name": "Headphones", "price": 199.99}
]

async def time_consuming_operation():
    time.sleep(10)

@router.post("/new")
def create_product(
    name: str = Form(...),
    price: float = Form(...)
):
    products.append({"name": name, "price": price})
    return products


@router.get("/all")
async def get_all_products():
    await time_consuming_operation()
    log("INFO", "Fetching all products")
    data = " ".join([product["name"] for product in products])
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/withheaders")
def get_products_with_headers(
        response: Response,
        custom_header: Optional[List[str]] = Header(None),
        test_cookie: Optional[str] = Cookie(None)
    ):
    if custom_header:
        response.headers["custom_response_header"] = " and ".join(custom_header)
    return {
        "data": products,
        "custom_header": custom_header,
        "test_cookie": test_cookie,
        "message": "Products with headers"
    }

@router.get("/{id}", responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product 1</div>"
            }
        },
        "description": "Return the product details in HTML format"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not found"
            }
        },
        "description": "Return a plain text message indicating the product was not found"
    }
})
def get_product_by_id(id: int):

    if id > len(products):
        out = "Product not found"
        return PlainTextResponse(content=out, media_type="text/plain", status_code=404)
    else:
        product = products[id]
        op = f"""
        <h1>{product}</h1>
        """
        return HTMLResponse(content=op, media_type="text/html")