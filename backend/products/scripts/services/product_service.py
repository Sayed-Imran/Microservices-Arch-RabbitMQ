from scripts.utils.security.jwt_util import JWT
from scripts.constants.api_endpoints import APIEnpoints
from scripts.schemas.products_schema import ProductsSchema
from fastapi import HTTPException, APIRouter, status, Depends
from scripts.core.handlers.product_handler import ProductsHandler

products_router = APIRouter(prefix=APIEnpoints.api)
jwt = JWT()


@products_router.get(APIEnpoints.find_products, status_code=status.HTTP_200_OK)
def find_products(user_data=Depends(jwt.get_current_user)):
    try:
        product_handler = ProductsHandler()
        return product_handler.find_products()
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)


@products_router.get(
    APIEnpoints.find_product + "/{product_id}", status_code=status.HTTP_200_OK
)
def find_product(product_id: str, user_data=Depends(jwt.get_current_user)):
    try:
        product_handler = ProductsHandler()
        return product_handler.find_one(product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)


@products_router.post(APIEnpoints.create_product, status_code=status.HTTP_201_CREATED)
def create_product(data: ProductsSchema, user_data=Depends(jwt.get_current_user)):
    try:
        product_handler = ProductsHandler()
        if product_handler.create_one(data.dict()):
            return data.dict()
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=e.args)


@products_router.put(
    APIEnpoints.update_product + "/{product_id}", status_code=status.HTTP_200_OK
)
def update_product(
    product_id: str, data: ProductsSchema, user_data=Depends(jwt.get_current_user)
):
    try:
        product_handler = ProductsHandler()
        if product_handler.update_one(product_id, data.dict()):
            return data.dict()
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=e.args)


@products_router.delete(
    APIEnpoints.delete_product + "/{product_id}", status_code=status.HTTP_202_ACCEPTED
)
def delete_product(product_id: str, user_data=Depends(jwt.get_current_user)):
    try:
        product_handler = ProductsHandler()
        if product_handler.delete_one(product_id):
            return {"status": "Successfully deleted"}
        else:
            raise

    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)
