import json
from scripts.utils.security.jwt_util import JWT
from scripts.constants.api_endpoints import APIEndpoints
from fastapi import HTTPException, status, APIRouter, Depends
from scripts.core.handlers.product_handler import ProductsHandler
from scripts.core.handlers.productUser_handler import ProductUserHandler

product_router = APIRouter(prefix=APIEndpoints.api)
jwt = JWT()

@product_router.post(
    APIEndpoints.like + "/{product_id}", status_code=status.HTTP_200_OK
)
def like_dislike(product_id: str,user_data=Depends(jwt.get_current_user)):
    try:
        product_user_handler = ProductUserHandler()
        product_user_handler.like_dislike_product(product_id, user_data['user_id'])
        return {"status": "Success"}
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.args)


@product_router.get(APIEndpoints.products, status_code=status.HTTP_200_OK)
def products(user_data=Depends(jwt.get_current_user)):
    try:
        prodcut_handler = ProductsHandler()
        return prodcut_handler.find_products()
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.args)
