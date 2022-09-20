import random
from fastapi import HTTPException, APIRouter, status
from scripts.core.handlers.product_handler import ProductsHandler
from scripts.constants.api_endpoints import APIEnpoints
from scripts.schemas.products_schema import ProductsSchema

products_router = APIRouter(prefix=APIEnpoints.api)

@products_router.get(APIEnpoints.find_products, status_code=status.HTTP_200_OK)
def find_products():
    try:
        product_handler = ProductsHandler()
        return product_handler.find_products()
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)

@products_router.get(APIEnpoints.find_product+"/{product_id}",status_code=status.HTTP_200_OK)
def find_product(product_id:str):
    try:
        product_handler = ProductsHandler()
        return product_handler.find_one(product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)

@products_router.post(APIEnpoints.create_product,status_code=status.HTTP_201_CREATED)
def create_product(data:ProductsSchema):
    try:
        product_handler = ProductsHandler()
        if product_handler.create_one(data.dict()):
            return data.dict()
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=e.args)

@products_router.put(APIEnpoints.update_product+"/{product_id}", status_code=status.HTTP_200_OK)
def update_product(product_id:str,data:ProductsSchema):
    try:
        product_handler = ProductsHandler()
        if product_handler.update_one(product_id,data.dict()):
            return data.dict()
        else:
            raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=e.args)

@products_router.delete(APIEnpoints.delete_product+"/{product_id}",status_code=status.HTTP_202_ACCEPTED)
def delete_product(product_id:str):
    try:
        product_handler = ProductsHandler()
        if product_handler.delete_one(product_id):
            return {"status":"Successfully deleted"}
        else:
            raise
    
    except Exception as e:
        print(e.args)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.args)


# Route for a random user
@products_router.get('/user')
def get_user():
    return {'id': random.choice([1,2,3,4,5,6])}