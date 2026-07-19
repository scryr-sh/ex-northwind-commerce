from northwind_api.catalog import Product


def score_checkout(
    *,
    order_total_cents: int,
    total_quantity: int,
    shipping_speed: str,
    products: list[Product],
) -> int:
    score = 12

    if order_total_cents > 100_000:
        score += 28
    if order_total_cents > 250_000:
        score += 24
    if total_quantity > 12:
        score += 18
    if shipping_speed == "expedited":
        score += 16
    if any(product.category == "Seafood" for product in products):
        score += 8

    return min(score, 100)
