from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ManePageCalc:
    def __init__(self, driver):
        self._driver = driver

    # окрываю сайт
    def open_calc(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # выставляю ожидание для калькулятора
    def wait_resp(self):
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        # delay.clear()
        delay.send_keys(Keys.BACKSPACE)
        delay.send_keys("45")

    # совершаю операцию в калькуляторе
    def operations(self):
        self._driver.find_element(By.XPATH, "//*[text()='7']").click()
        self._driver.find_element(By.XPATH, "//*[text()='+']").click()
        self._driver.find_element(By.XPATH, "//*[text()='8']").click()
        self._driver.find_element(By.XPATH, "//*[text()='=']").click()

    # выставление ожидания ответа
    def waiting_resp(self):
        WebDriverWait(self._driver, 48).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15'))

    # сравнение результата
    def result(self):
        result = self._driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]').text
        assert int(result) == 15
