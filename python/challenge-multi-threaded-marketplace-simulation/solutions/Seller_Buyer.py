import threading
import time
from typing import List
from Catalog import Catalog

# defines a product class with id, name and price attributes 
class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Seller(threading.Thread):
    # the seller class inherits from threading.thread and has an identifier and a catalog attribute.
    def __init__(self, id: int, catalog: Catalog):
        super().__init__()
        self.id = id
        self.catalog = catalog

    # this method adds new products to the product catalog.
    def add_product(self, product: Product) -> None:
        self.catalog.add_product(product)

    # the run method creates three new products with names and prices that are incremented in multiples of 10.
    # each product is then added to the product catalog and prints a message to show that it was added.
    # the thread sleeps for one second after each product is added.
    def run(self) -> None:
        for i in range(1, 4):
            product = Product(i, f"Product {i}", i * 10.0)
            self.add_product(product)
            print(f"Seller {self.id} added {product.name}")
            time.sleep(1)

class Buyer(threading.Thread):
    # define __init__ method to set instance variables id and catalog.
    def __init__(self, id: int, catalog: Catalog):
        super().__init__()
        self.id = id
        self.catalog = catalog

    # define a method browse_catalog which calls the browse_catalog method of self.catalog.
    # the return type is list of product type. 
    def browse_catalog(self) -> List[Product]:
        return self.catalog.browse_catalog()

    # define a method buy_product which accepts an integer product_id as argument.
    # this method tries to get a product from self.catalog with the help of get_product method.
    # if product exists then print a message to console mentioning buyer id and name of product.
    # finally remove that product from catalog.
    def buy_product(self, product_id: int) -> None:
        product = self.catalog.get_product(product_id)
        if product:
            print(f"Buyer {self.id} bought {product.name}")
            self.catalog.remove_product(product_id)

    # define run method which is overriden from the thread class.
    # sleep for 2 seconds, call browse_catalog and store the results in variable.
    # iterate over each product, call buy_product method and sleep for 1 second.
    def run(self) -> None:
        time.sleep(2)
        products = self.browse_catalog()
        for product in products:
            self.buy_product(product.id)
            time.sleep(1)
            
if __name__ == "__main__":
    catalog = Catalog()
    sellers = [Seller(i, catalog) for i in range(1, 4)]
    buyers = [Buyer(i, catalog) for i in range(1, 4)]

    for seller in sellers:
        seller.start()

    for buyer in buyers:
        buyer.start()

    for seller in sellers:
        seller.join()

    for buyer in buyers:
        buyer.join()

    catalog.display_catalog()
