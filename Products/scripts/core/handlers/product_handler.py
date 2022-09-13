import string, random
from products.scripts.utils.producer_util import publish
from scripts.db.mongo.microservice1.collections.products import Products
from scripts.db.mongo import mongo_client


class ProductsHandler:
    def __init__(self) -> None:
        self.products = Products(mongo_client)

    def find_products(self):
        try:
            return self.products.find_all_products()
        except Exception as e:
            print(e.args)
            return None

    def find_one(self, product_id: str):
        try:
            return self.products.find_product(product_id)
        except Exception as e:
            print(e.args)
            return None

    def create_one(self, data: dict):
        try:
            product_id = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=7)
            )
            data["product_id"] = product_id
            self.products.create_product(data)
            publish("product_created", data)
            return True
        except Exception as e:
            print(e.args)
            return False

    def update_one(self, product_id: str, data: dict):
        try:
            self.products.update_product(product_id, data)
            data["product_id"] = product_id
            publish("product_updated", data)
            return True
        except Exception as e:
            print(e.args)
            return False

    def delete_one(self, product_id: str):
        try:
            self.products.delete_product(product_id)
            publish("product_deleted", {"product_id": product_id})
            return True
        except Exception as e:
            print(e.args)
            return False