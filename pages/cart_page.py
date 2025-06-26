from pages.base_page import BasePage


class Cart(BasePage):
    CHECKOUT_SELECTOR = "//button[@id='checkout']"
    FNAME_SELECTOR = "//input[@id='first-name']"
    LNAME_SELECTOR = "//input[@id='last-name']"
    POSTALCODE_SELECTOR = "//input[@id='postal-code']"
    CONTINUE_SELECTOR = "//input[@id='continue']"
    FINISH_SELECTOR = "//button[@id='finish']"

    def checkout(self):
        self.click(self.CHECKOUT_SELECTOR)
        self.fill(self.FNAME_SELECTOR,"Jeel")
        self.fill(self.LNAME_SELECTOR,"Bhuptani")
        self.fill(self.POSTALCODE_SELECTOR,"362560")
        self.click(self.CONTINUE_SELECTOR)
        self.click(self.FINISH_SELECTOR)
