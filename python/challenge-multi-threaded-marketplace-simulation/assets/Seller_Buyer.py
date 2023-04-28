# Importing necessary modules including threading,time and required type hints
import threading
import time
from typing import List
# Importing Catalog class from a module called Catalog
from Catalog import Catalog
# Importing Product class from a module called Product
from Product import Product

class Seller(threading.Thread):
    def __init__(self, id: int, catalog: Catalog):

        # TODO: Write your code here
        pass

    def add_product(self, product: Product) -> None:

        # TODO: Write your code here
        pass

    def run(self) -> None:

        # TODO: Write your code here
        pass


class Buyer(threading.Thread):
    def __init__(self, id: int, catalog: Catalog):

        # TODO: Write your code here
        pass

    def browse_catalog(self) -> List[Product]:

        # TODO: Write your code here
        pass

    def buy_product(self, product_id: int) -> None:

        # TODO: Write your code here
        pass

    def run(self) -> None:

        # TODO: Write your code here
        pass


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