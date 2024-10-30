# pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    checkout_button = (By.ID, "hlb-ptc-btn-native")

    def proceed_to_checkout(self):
        self.click(self.checkout_button)

    def is_checkout_page_displayed(self):
        # Placeholder for checkout page verification
        return True
