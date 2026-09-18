def calculate_total(unit_price, quantity, discount_percent=0):
    if quantity < 0:
        raise ValueError("quantity must be positive")

    discount_percent = min(max(discount_percent, 0), 100)

    subtotal = unit_price * quantity
    total = subtotal * (1 - discount_percent / 100)

    return round(total, 2)