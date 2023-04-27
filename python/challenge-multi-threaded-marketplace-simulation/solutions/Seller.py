import threading
import time
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

if __name__ == "__main__":
    sellers = [Seller(i, Catalog) for i in range(1, 4)]

    for seller in sellers:
        seller.start()

    for seller in sellers:
        seller.join()