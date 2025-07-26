from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(driver):
    # переход на сайт
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(4)

    # авторизация на сайте
    driver.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()

    # добавление товаров в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # перейти в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container").click()
    # or driver.get("https://www.saucedemo.com/cart.html")

    # chekout
    driver.find_element(
        By.CSS_SELECTOR, "#checkout").click()

    # Запонение полей ввода данных пользователя
    driver.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Tatiana")
    driver.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Goryashina")
    driver.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("670045")

    # нажимаю продолжить
    driver.find_element(
        By.CSS_SELECTOR, "#continue").click()

    # прочесть total
    txt = driver.find_element(
        By.CSS_SELECTOR, '[data-test="total-label"]').text

    # сравнение значения total
    assert txt == "Total: $58.29"
