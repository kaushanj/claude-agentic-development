def calculate_total(unit_price, quantity, discount_percent=0):
    if quantity < 0:
        raise ValueError("quantity must be positive")
    if unit_price < 0:
        raise ValueError("unit_price must be positive")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    subtotal = unit_price * quantity
    total = subtotal * (1 - discount_percent / 100)

    return round(total, 2)