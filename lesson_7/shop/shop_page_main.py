from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

class main:
    def add_products():
        # добавление товаров в корзину
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart():
            # перейти в корзину
        driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
        # or driver.get("https://www.saucedemo.com/cart.html")