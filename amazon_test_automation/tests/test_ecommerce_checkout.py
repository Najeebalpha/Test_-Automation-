# tests/test_ecommerce_checkout.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.fixture(scope="module")
def setup():
    # Set up Chrome WebDriver with WebDriverManager for automatic driver management
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.amazon.com")
    yield driver
    driver.quit()


# Retry up to 3 times with a 2-second delay
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_add_product_to_cart(setup):
    driver = setup
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    # Step 1: Search for a product
    home_page.search_product("Laptop")

    # Step 2: Select the first product from results
    product_page.select_first_product()

    # Step 3: Add the selected product to the cart
    product_page.add_to_cart()

    # Step 4: Proceed to checkout
    cart_page.proceed_to_checkout()

    # Verify if the checkout page is displayed
    assert cart_page.is_checkout_page_displayed(), "Checkout page not displayed"
