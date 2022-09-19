from scripts.constants import DatabasesNames, CollectionNames
from scripts.db.mongo.schema import MongoBaseSchema
from scripts.utils.mongo_util import MongoCollectionBaseClass


class UserSchema(MongoBaseSchema):
    name: str
    email: str
    password: str
    


class Users(MongoCollectionBaseClass):
    def __init__(self, mongo_client):
        super().__init__(
            mongo_client=mongo_client,
            database=DatabasesNames.microservice0,
            collection=CollectionNames.users,
        )

    def find_all_users(self):
        users = self.find(query={})
        if users:
            return list(users)

    def find_user(self, user_id):
        user = self.find_one(query={"user_id": user_id})
        if user:
            return user

    def create_user(self, data: dict):
        self.insert_one(data=data)

    def delete_user(self, user_id):
        self.delete_one(query={"user_id": user_id})