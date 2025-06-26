from pages.base_page import BasePage


class Login(BasePage):
    EMAIL_SELECTOR = "//input[@id='user-name']"
    PASSWORD_SELECTOR = "//input[@id='password']"
    LOGIN_BUTTON_SELECTOR = "//input[@id='login-button']"

    def login(self, email, password):
        self.fill(self.EMAIL_SELECTOR, email)
        self.fill(self.PASSWORD_SELECTOR, password)
        self.click(self.LOGIN_BUTTON_SELECTOR)



