from scripts.db.mongo.microservice2.collections.product import Products
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
            self.products.create_product(data)
            return True
        except Exception as e:
            print(e.args)
            return False

    def update_one(self, product_id: str, data: dict):
        try:
            self.products.update_product(product_id, data)
            return True
        except Exception as e:
            print(e.args)
            return False

    def delete_one(self, product_id: str):
        try:
            self.products.delete_product(product_id)
            return True
        except Exception as e:
            print(e.args)
            return False
