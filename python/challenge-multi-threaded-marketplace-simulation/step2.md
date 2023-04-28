# Implementing the Catalog

In this sub-challenge, you will implement the `Catalog` class. The `Catalog` class should manage the shared data structure containing product listings. It should provide thread-safe methods for adding, removing, and updating products, as well as browsing the catalog.

## Example

Suppose we have an online shopping platform that uses this Catalog class to manage its products. A new product, "Wireless Earbuds", with the id of 1234, name of "X-earbuds", and a price of $49.99, is added to the platform.

```python
catalog = Catalog() # create a new instance of the Catalog class
new_product = Product(1234, "X-earbuds", 49.99) # create a new product object
catalog.add_product(new_product) # add the new product to the catalog
```

Then, a user searches for a product with the id of 1234.

```python
search_result = catalog.get_product(1234) # retrieve the product object with id 1234
if search_result: # check if the product exists in the catalog
print(f"Product Found: {search_result.name}, Price: ${search_result.price}")
```

Output:

```python
Product Found: X-earbuds, Price: $49.99
```

## TODO

- Complete `Catalog.py`

## Requirements

- Create a `Catalog` class with methods to add, remove, update, and browse products.
- Implement proper synchronization mechanisms to ensure thread-safe access to the shared product listings.
- Implement a method to display the current state of the catalog.
