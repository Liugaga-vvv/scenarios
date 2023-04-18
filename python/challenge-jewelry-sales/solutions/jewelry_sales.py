from typing import List, Tuple


def process_sales_data(
    sales: List[Tuple[str, int, float]]
) -> Tuple[float, int, float, str]:
    if not sales:
        return 0.0, 0, 0.0, ""

    total_revenue = 0.0
    total_quantity = 0
    product_sales = {}

    for product, quantity, price in sales:
        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be positive.")
        total_revenue += quantity * price
        total_quantity += quantity
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

    average_price = (
        round(total_revenue / total_quantity, 2) if total_quantity > 0 else 0.0
    )
    most_popular_product = max(product_sales, key=product_sales.get)

    return total_revenue, total_quantity, average_price, most_popular_product
