import threading
from typing import Dict, List, Optional


class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Catalog:
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.lock = threading.Lock()

    def add_product(self, product: Product) -> None:
        with self.lock:
            self.products[product.id] = product

    def remove_product(self, product_id: int) -> None:
        with self.lock:
            del self.products[product_id]

    def get_product(self, product_id: int) -> Optional[Product]:
        with self.lock:
            return self.products.get(product_id)

    def browse_catalog(self) -> List[Product]:
        with self.lock:
            return list(self.products.values())

    def display_catalog(self) -> None:
        with self.lock:
            print("Catalog:")
            for product in self.products.values():
                print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}")

if __name__ == "__main__":
    catalog = Catalog()
    catalog.display_catalog()