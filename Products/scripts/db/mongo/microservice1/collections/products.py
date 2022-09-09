from scripts.constants import CollectionNames, DatabasesNames
from scripts.db.mongo.schema import MongoBaseSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class ProductSchema(MongoBaseSchema):
    title: str
    image: str
    likes: int = 0

class Products(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        super().__init__(
            mongo_client=mongo_client,
            database=DatabasesNames.microservice1,
            collection=CollectionNames.products,
        )

    def find_all_products(self):
        products = self.find(query={})
        if products:
            return list(products)

    def find_product(self,  product_id):
        product = self.find_one(query={"product_id":product_id})
        if product:
            return product

    def create_product(self, data: dict):
        self.insert_one(data=data)
    
    def update_product(self,product_id,data:dict):
        self.update_one(query={"product_id":product_id}, data=data, upsert=False)
    
    def delete_product(self,product_id):
        self.delete_one(query={"product_id":product_id})