from scripts.constants import CollectionNames, DatabasesNames
from scripts.db.mongo.schema import MongoBaseSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class ProductUserSchema(MongoBaseSchema):
    product_id: str
    users: list = []


class ProductUser(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        super().__init__(
            mongo_client=mongo_client,
            database=DatabasesNames.microservice2,
            collection=CollectionNames.productUser,
        )

    def find_all_products(self):
        products = self.find(query={})
        if products:
            return list(products)

    def find_product(self, product_id):
        product = self.find_one(query={"product_id": product_id})
        if product:
            return product

    def create_product(self, data: dict):
        self.insert_one(data=data)

    def delete_product(self, product_id):
        self.delete_one(query={"product_id": product_id})

    def like_product(self,product_id:str,user_id:str):
        self.update_push_array(query={"product_id":product_id},array_key='users',data=user_id)

    def dislike_product(self,product_id,user_id:str):
        self.update_pull_array(query={"product_id":product_id},array_key='users',data=user_id)