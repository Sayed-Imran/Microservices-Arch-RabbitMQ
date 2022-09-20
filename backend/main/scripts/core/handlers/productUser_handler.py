from scripts.db.mongo.microservice2.collections.productUser import ProductUser
from scripts.db.mongo import mongo_client
from scripts.utils.producer_util import Publisher
from scripts.constants.app_configuration import MicroService

publisher = Publisher(MicroService.RabbitMQ.uri)


class ProductUserHandler:
    def __init__(self) -> None:
        self.productUser = ProductUser(mongo_client)

    def create_product(self, data):
        try:
            self.productUser.create_product(data)
            return True
        except Exception as e:
            print(e.args)
            return False

    def delete_product(self,product_id):
        try:
            self.productUser.delete_product(product_id)
            return True
        except Exception as e:
            print(e.args)
            return False

    def like_dislike_product(self, product_id: str, user_id: str):
        try:
            product = self.productUser.find_product(product_id)
            if user_id in product["users"]:
                self.productUser.dislike_product(product_id, user_id)
                publisher.publish("product_disliked", {"product_id": product_id})
            else:
                self.productUser.like_product(product_id, user_id)
                publisher.publish("product_liked", {"product_id": product_id})
            return True
        except Exception as e:
            print(e.args)
            return False
