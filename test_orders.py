from orders import order_total, is_free_delivery
def test_order_total():
    assert order_total(999, 40) == 290
def test_free_delivery_yes():
    assert is_free_delivery(500) == True
def test_free_delivery_no():
    assert is_free_delivery(300) == False