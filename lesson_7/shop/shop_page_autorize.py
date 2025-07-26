from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

class autorize:
    def open_shop(driver):
        # переход на сайт
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(4)

    def auto():
            # авторизация на сайте
        driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()