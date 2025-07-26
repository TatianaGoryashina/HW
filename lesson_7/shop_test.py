from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from shop_page_autorize import autorize
from shop_page_main import main
from shop_page_cart import cart
from shop_page_final import final

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

driver.open_shop()
driver.autorize()
driver.add_products()
driver.go_to_cart()
driver.checkout()