def calculate_shipping(weight):
    if type(weight) is not int or not 1 <= weight <= 50:
        raise ValueError("weight must be between 1 and 50")
    return 5.00
