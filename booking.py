def calculate_total(price, tickets):
    if price <= 0 or tickets <= 0:
        raise ValueError("Invalid price or ticket count")
    return price * tickets
