# Importing necessary modules including threading and required type hints
import threading
from typing import Dict, List, Optional
# Importing Product class from a module called Product
from Product import Product

# defines a catalog class that stores products in a dictionary called `products` and provides methods to manipulate it
class Catalog:
    def __init__(self):
        # initialize an empty dictionary 'products' to store product objects keyed by their ids.
        self.products: Dict[int, Product] = {}
        # initialize a lock for the catalog to prevent race conditions in multi-threaded usage
        self.lock = threading.Lock()

    # method to add a product to the catalog's `products` dictionary
    def add_product(self, product: Product) -> None:
        # use a lock to ensure this block of code is executed as one atomic operation to avoid race conditions.
        with self.lock:
            self.products[product.id] = product

    # method to remove a specific product from the catalog by its id value
    def remove_product(self, product_id: int) -> None:
        # use a lock to ensure this block of code is executed as one atomic operation to avoid race conditions.
        with self.lock:
            del self.products[product_id]

    # method to retrieve a product object stored in the catalog given a specific product id
    # this method returns none if the product is not found in the catalog.
    def get_product(self, product_id: int) -> Optional[Product]:
        # use a lock to ensure this block of code is executed as one atomic operation to avoid race conditions.
        with self.lock:
            return self.products.get(product_id)

    # method to return all products stored in the catalog as a list of product objects.
    def browse_catalog(self) -> List[Product]:
        # use a lock to ensure this block of code is executed as one atomic operation to avoid race conditions.
        with self.lock:
            return list(self.products.values())

    # method to display all products stored in the catalog formatted for human-readable output.
    def display_catalog(self) -> None:
        # use a lock to ensure this block of code is executed as one atomic operation to avoid race conditions.
        with self.lock:
            print("Catalog:")
            # iterate over all product objects stored in the catalog and print their id, name
            for product in self.products.values():
                print(
                    f"ID: {product.id}, Name: {product.name}, Price: ${product.price}")


if __name__ == "__main__":
    catalog = Catalog()
    catalog.display_catalog()
