import math


def calculate_total(unit_price, quantity, discount_percent=0):
    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("quantity must be positive")
    if quantity > 75:
        raise ValueError("quantity must not exceed 75")
    if isinstance(unit_price, bool):
        raise ValueError("unit_price must be non-negative")
    if not isinstance(unit_price, (int, float)):
        raise ValueError("unit_price must be non-negative")
    if not math.isfinite(unit_price):
        raise ValueError("unit_price must be non-negative")
    if unit_price < 0:
        raise ValueError("unit_price must be non-negative")

    if isinstance(discount_percent, bool) or not isinstance(discount_percent, int):
        raise ValueError("discount_percent must be between 0 and 100")
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    subtotal = unit_price * quantity
    total = subtotal * (1 - discount_percent / 100)

    return round(total, 2)
