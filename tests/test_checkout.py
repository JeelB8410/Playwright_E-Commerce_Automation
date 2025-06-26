import pytest
from pages.cart_page import Cart
import pytest_asyncio


# @pytest.mark.asyncio
@pytest.mark.order(4)
def test_checkout(page_custome):
    checkout = Cart(page_custome)
    checkout.checkout()
    print(page_custome.title())
    assert page_custome.is_visible("//h2[text()='Thank you for your order!']")
    print("Test Run Succesfully")


