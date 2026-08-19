from cart import cart_total, apply_discount
def test_cart_total():
    items = [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]
    assert cart_total(items) == 999
def test_apply_discount():
    assert apply_discount(200, 10) == 180
def test_zero_discount():
    assert apply_discount(100, 0) == 100