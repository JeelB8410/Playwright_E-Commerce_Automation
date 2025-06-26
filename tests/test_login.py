import time

import pytest
from pages.login_page import Login
import pytest_asyncio


# @pytest.mark.asyncio
@pytest.mark.order(1)
def test_login(page_custome):
    login = Login(page_custome)
    print("Going")
    login.login("standard_user","secret_sauce")
    time.sleep(5)
    assert page_custome.is_visible("//span[@class='title']")

