# pages/home_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    search_box = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")

    def search_product(self, product_name):
        self.enter_text(self.search_box, product_name)
        self.click(self.search_button)
