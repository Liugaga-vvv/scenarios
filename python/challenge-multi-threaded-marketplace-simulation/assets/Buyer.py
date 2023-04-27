import threading
import time
from typing import List
from Catalog import Catalog

class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

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

    buyers = [Buyer(i, Catalog) for i in range(1, 4)]

    for buyer in buyers:
        buyer.start()
        
    for buyer in buyers:
        buyer.join()
