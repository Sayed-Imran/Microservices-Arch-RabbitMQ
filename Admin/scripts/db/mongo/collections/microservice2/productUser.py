from scripts.constants import CollectionNames, DatabasesNames
from scripts.db.mongo.schema import MongoBaseSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class ProductUserSchema(MongoBaseSchema):
    user_id: str
    product_id: str


class ProductUser(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        super().__init__(
            mongo_client=mongo_client,
            database=DatabasesNames.microservice2,
            collection=CollectionNames.productUser,
        )

    def find_all_users(self):
        users = self.find(query={})
        if users:
            return list(users)

    def find_user(self,  id):
        user = self.find_one(query={"id":id})
        if user:
            return user

    def create_user(self, data: dict):
        self.insert_one(data=data)
    
    def update_user(self,id,data:dict):
        self.update_one(query={"id":id}, data=data, upsert=False)
    
    def delete_user(self,id):
        self.delete_one(query={"id":id})