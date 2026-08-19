def order_total(cart_amount, delivery_fee):
    return cart_amount + delivery_fee
def is_free_delivery(cart_amount):
    return cart_amount >= 500