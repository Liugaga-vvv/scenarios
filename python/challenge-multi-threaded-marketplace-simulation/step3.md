# Implementing the Seller

In this sub-challenge, you will implement the `Seller` class. The `Seller` class should create new product listings and update the shared catalog. Each seller will run in a separate thread and should be able to add products to the catalog without conflicts.

## TODO

- Complete `Seller.py`

## Requirements

- Create a `Seller` class with a unique ID and a method to add products to the catalog.
- Implement the `run` method for the `Seller` class, which will be executed in a separate thread.
- Ensure proper synchronization when adding products to the shared catalog.
