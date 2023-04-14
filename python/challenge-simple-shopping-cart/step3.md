# Apply Discounts

In this step, you will extend the ShoppingCart class to apply discounts. Discounts can be percentage-based or fixed-amount based. You will implement two methods, one for applying percentage-based discounts and another for applying fixed-amount discounts.

### Example

```python
cart = ShoppingCart()
cart.add_product(Product("Apple", 0.5))
cart.add_product(Product("Orange", 0.6))
cart.apply_percentage_discount(10)
print(cart.total())  # Output: 0.99
cart.apply_fixed_discount(0.2)
print(cart.total())  # Output: 0.79
```

### Requirements

1. Add two methods to the `ShoppingCart` class: `apply_percentage_discount` and `apply_fixed_discount`.
2. The `apply_percentage_discount` method should take a percentage (float) and reduce the price of each product in the cart by that percentage.
3. The `apply_fixed_discount` method should take a fixed discount amount (float) and reduce the total cost of the products in the cart by that amount.
4. Add appropriate docstrings and type hints for all methods.

Now you have a simple shopping cart system that can handle adding and removing products, as well as applying different types of discounts. Students can use this case to practice object-oriented programming and gain a deeper understanding of Python classes and methods.
