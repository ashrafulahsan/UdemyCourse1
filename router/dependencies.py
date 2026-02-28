from fastapi import APIRouter, Depends, Request
from websockets import headers

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"]
)

def convert_query_params(request: Request, separetor: str = " --:-- "):
    out_query_params = []
    for key, value in request.query_params.items():
        out_query_params.append(f"{key} {separetor} {value}")
    return out_query_params

def convert_headers(request: Request, separetor: str = " --:-- ", query = Depends(convert_query_params)):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {separetor} {value}")
    return {
        "headers": out_headers,
        "query_params": query
    }

@router.get("/headers")
def get_headers(test: str, separetor: str = '$$$', headers: list[str] = Depends(convert_headers)):
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

class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

@router.get("/user")
def get_user(name: str, email: str, account: Account = Depends(Account)):
    return {
        'account': {
            'name': account.name,
            'email': account.email
        }
    }