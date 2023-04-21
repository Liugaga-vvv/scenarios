# Jewelry Sales

## Introduction

You work for a small business that sells handmade jewelry. They have asked you to help them create a program that will track their sales data. The business currently uses a spreadsheet to manage their sales data, but they are finding it difficult to keep up with the increasing volume of sales. Your task is to create a Python program that will process the sales data and provide useful insights to help the business make informed decisions.

## Problem Description

You will be given a list of tuples, where each tuple represents a sale. Each tuple contains the following information:

- the name of the product sold (a string)
- the quantity sold (an integer)
- the price per unit (a float)

Your program should process this data and provide the following information:

- the total revenue generated from sales
- the total quantity of products sold
- the average price per unit sold
- the most popular product (i.e., the product that was sold the most)

## Requirements

- Define a function `process_sales_data(sales: List[Tuple[str, int, float]]) -> Tuple[float, int, float, str]` that takes in a list of sales data and returns a tuple of the form `(total_revenue: float, total_quantity: int, average_price: float, most_popular_product: str)`
- The function should be able to handle an empty sales list and return `(0.0, 0, 0.0, '')`.
- The function should raise a `ValueError` if any of the quantities or prices are negative.
- The function should round the average price to two decimal places.

## Example Usage

```
# Test case 1: Empty sales list
assert process_sales_data([]) == (0.0, 0, 0.0, '')

# Test case 2: One sale
assert process_sales_data([('Necklace', 1, 15.50)]) == (15.50, 1, 15.50, 'Necklace')

# Test case 3: Multiple sales of same product
assert process_sales_data([('Earrings', 2, 10.00), ('Earrings', 1, 10.00), ('Earrings', 3, 10.00)]) == (60.00, 6, 10.00, 'Earrings')

# Test case 4: Multiple sales of different products
assert process_sales_data([('Bracelet', 1, 12.00), ('Earrings', 2, 8.50), ('Necklace', 3, 20.00)]) == (89.0, 6, 14.83, 'Necklace')
```
