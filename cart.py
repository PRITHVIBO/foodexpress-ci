def cart_total(items):
    total = 0
    for item in items:
        total = total + item["price"] * item["qty"]
    return total
def apply_discount(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return total - (total * percent / 100)