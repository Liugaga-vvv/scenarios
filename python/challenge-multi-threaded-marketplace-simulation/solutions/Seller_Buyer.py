import threading
import time
from typing import List
from Catalog import Catalog

class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Seller(threading.Thread):
    def __init__(self, id: int, catalog: Catalog):
        super().__init__()
        self.id = id
        self.catalog = catalog

    def add_product(self, product: Product) -> None:
        self.catalog.add_product(product)

    def run(self) -> None:
        for i in range(1, 4):
            product = Product(i, f"Product {i}", i * 10.0)
            self.add_product(product)
            print(f"Seller {self.id} added {product.name}")
            time.sleep(1)
            
class Buyer(threading.Thread):
    def __init__(self, id: int, catalog: Catalog):
        super().__init__()
        self.id = id
        self.catalog = catalog

    def browse_catalog(self) -> List[Product]:
        return self.catalog.browse_catalog()

    def buy_product(self, product_id: int) -> None:
        product = self.catalog.get_product(product_id)
        if product:
            print(f"Buyer {self.id} bought {product.name}")
            self.catalog.remove_product(product_id)

    def run(self) -> None:
        time.sleep(2)
        products = self.browse_catalog()
        for product in products:
            self.buy_product(product.id)
            time.sleep(1)


if __name__ == "__main__":

    sellers = [Seller(i, Catalog) for i in range(1, 4)]
    buyers = [Buyer(i, Catalog) for i in range(1, 4)]

    for seller in sellers:
        seller.start()

    for buyer in buyers:
        buyer.start()

    for seller in sellers:
        seller.join()
        
    for buyer in buyers:
        buyer.join()