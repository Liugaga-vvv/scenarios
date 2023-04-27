import threading
from typing import Dict, List, Optional

class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

class Catalog:
    def __init__(self):

        # TODO: Write your code here
        pass 

    def add_product(self, product: Product) -> None:
         
        # TODO: Write your code here
        pass 

    def remove_product(self, product_id: int) -> None:
         
        # TODO: Write your code here
        pass 

    def get_product(self, product_id: int) -> Optional[Product]:
         
        # TODO: Write your code here
        pass 

    def browse_catalog(self) -> List[Product]:
         
        # TODO: Write your code here
        pass 

    def display_catalog(self) -> None:
        
        # TODO: Write your code here
        pass 

if __name__ == "__main__":
    catalog = Catalog()
    catalog.display_catalog()