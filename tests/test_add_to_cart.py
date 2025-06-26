import pytest
from pages.product_page import AddToCart
import pytest_asyncio


# @pytest.mark.asyncio
@pytest.mark.order(3)
def test_add_to_cart(page_custome):
    product = AddToCart(page_custome)
    product.add_to_cart()

