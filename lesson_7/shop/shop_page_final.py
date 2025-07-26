from selenium import webdriver
from selenium.webdriver.common.by import By


class final:
    def fill_input_field():
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

    def total():
        # прочесть total
        txt = driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        # сравнение значения total
        assert txt == "Total: $58.29"