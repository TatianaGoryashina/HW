from selenium.webdriver.common.by import By


class final:
    def __init__(self, driver):
        self.driver = driver

    def fill_input_field(self):
        # Запонение полей ввода данных пользователя
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Tatiana")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Goryashina")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("670045")
        # нажимаю продолжить
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()

    def total(self):
        # прочесть total
        txt = self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        # сравнение значения total
        assert txt == "Total: $58.29"
