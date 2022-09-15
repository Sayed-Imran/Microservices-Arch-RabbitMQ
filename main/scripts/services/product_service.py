import json
import requests
from main.scripts.core.handlers.productUser_handler import ProductUserHandler
from fastapi import HTTPException, status, APIRouter
from scripts.constants.api_endpoints import APIEndpoints

product_router = APIRouter(prefix=APIEndpoints.api)


@product_router.post(APIEndpoints.create_product,status_code=status.HTTP_201_CREATED)
def create_product(product_id:str):
    try:
        product_user_handler = ProductUserHandler()
        if product_user_handler.create_product({"product_id":product_id,'likes':[]}):
            return {
                "status":"Success"
            }
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args)



@product_router.post(
    APIEndpoints.like + "/{product_id}", status_code=status.HTTP_200_OK
)
def like_dislike(product_id: str):
    try:
        req = requests.get("http://localhost:8080/api/user").text
        user_id = json.loads(req)["id"]
        product_user_handler = ProductUserHandler()
        product_user_handler.like_dislike_product(product_id, user_id)
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args)
