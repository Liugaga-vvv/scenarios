# Create a ShoppingCart Class

Now that you have a Product class, it's time to create a ShoppingCart class. The ShoppingCart class should be able to add products, remove products, and calculate the total cost of the products in the cart.

### Example

```python
cart = ShoppingCart()
cart.add_product(Product("Apple", 0.5))
cart.add_product(Product("Orange", 0.6))
print(cart.total())  # Output: 1.1
cart.remove_product("Apple")
print(cart.total())  # Output: 0.6
```

### Requirements

1. Create a `ShoppingCart` class with an empty list attribute called `products`.
2. Add the following methods to the `ShoppingCart` class: `add_product`, `remove_product`, and `total`.
3. The `add_product` method should take a Product object and append it to the `products` list.
4. The `remove_product` method should take a product name (string) and remove the first matching product from the `products` list.
5. The `total` method should return the sum of the prices of all products in the `products` list.
6. Add appropriate docstrings and type hints for all methods.
