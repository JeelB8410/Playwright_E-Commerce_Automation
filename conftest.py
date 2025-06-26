import pytest
import pytest_asyncio
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser_context():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="session")
def page_custome(browser_context):
    context = browser_context.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    context.close()

