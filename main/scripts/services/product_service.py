from scripts.core.handlers.product_handler import ProductsHandler
from fastapi import HTTPException, status, APIRouter
from scripts.constants.api_endpoints import APIEndpoints
import requests

product_router = APIRouter(prefix=APIEndpoints.api)


@product_router.get(APIEndpoints.products, status_code=status.HTTP_200_OK)
def get_products():
    try:
        product_handler = ProductsHandler()
        product_handler.find_products()

    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)

@product_router.post(APIEndpoints.like+"{product_id}",status_code=status.HTTP_200_OK)
def like(product_id:str):