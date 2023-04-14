# Solution

```python
class Product:
    def __init__(self, name: str, price: float):
        """
        Initialize a new Product object.

        :param name: The name of the product.
        :type name: str
        :param price: The price of the product.
        :type price: float
        """
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        """
        Initialize a new ShoppingCart object.
        """
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: The product to be added.
        :type product: Product
        """
        self.products.append(product)

    def remove_product(self, product_name: str):
        """
        Remove a product from the shopping cart by name.

        :param product_name: The name of the product to be removed.
        :type product_name: str
        """
        for i, product in enumerate(self.products):
            if product.name == product_name:
                del self.products[i]
                break

    def total(self) -> float:
        """
        Calculate the total cost of the products in the shopping cart.

        :return: The total cost.
        :rtype: float
        """
        return sum(product.price for product in self.products)
```
