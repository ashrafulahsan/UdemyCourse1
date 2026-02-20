from fastapi import APIRouter, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional

router = APIRouter(
    prefix="/products", 
    tags=["products"]
)

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Smartphone", "price": 499.99},
    {"name": "Headphones", "price": 199.99}
]

# @router.get("/all")
# def get_all_products():
#     data = " ".join(products)
#     return Response(content=data, media_type="text/plain")


@router.get("/withheaders")
def get_products_with_headers(
        response: Response,
        custon_header: Optional[str] = Header(None)
    ):
    return {"message": "Products with headers"}

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