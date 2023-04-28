# Implementing the Seller and Buyer

In this sub-challenge, you will implement the `Seller` and `Buyer` class.

The `Seller` class should create new product listings and update the shared catalog. Each seller will run in a separate thread and should be able to add products to the catalog without conflicts.

The `Buyer` class should be able to browse the shared catalog and make purchases. Each buyer will run in a separate thread and should be able to purchase products without conflicts.

## TODO

- Complete `Seller_Buyer.py`

## Requirements

- Create a `Seller` class with a unique ID and a method to add products to the catalog.
- Implement the `run` method for the `Seller` and `Buyer` class, which will be executed in a separate thread.
- Ensure proper synchronization when adding products to the shared catalog.
- Create a `Buyer` class with a unique ID and methods to browse the catalog and make purchases.
- Ensure proper synchronization when browsing the catalog and making purchases.
