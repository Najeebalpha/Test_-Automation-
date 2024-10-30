# pages/product_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    first_product_link = (By.CLASS_NAME, "a-link-normal.s-no-outline")
    add_to_cart_button = (By.ID, "add-to-cart-button")

    def select_first_product(self):
        self.click(self.first_product_link)

    def add_to_cart(self):
        self.click(self.add_to_cart_button)
