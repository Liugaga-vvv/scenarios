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
         
        # TODO: Write your code here
        pass 

    def add_product(self, product: Product) -> None:
          
        # TODO: Write your code here
        pass 

    def run(self) -> None:
         
        # TODO: Write your code here
        pass 

if __name__ == "__main__":

    sellers = [Seller(i, Catalog) for i in range(1, 4)]

    for seller in sellers:
        seller.start()

    for seller in sellers:
        seller.join()