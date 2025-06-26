from pages.base_page import BasePage


class AddToCart(BasePage):
    PRODUCT_SELECTOR = "//div[text()='Sauce Labs Backpack']"
    ADD_TO_CART_SELECTOR = "//button[@id='add-to-cart']"
    ADD_TO_CART_LOGO_SELECTOR = "//span[@class='shopping_cart_badge']"

    def add_to_cart(self):
        self.click(self.PRODUCT_SELECTOR)
        self.click(self.ADD_TO_CART_SELECTOR)
        self.click(self.ADD_TO_CART_LOGO_SELECTOR)
