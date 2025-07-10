from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_wair_calc(driver):
    # go to page
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(4)

    # find element by locator
    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.send_keys(Keys.BACKSPACE)
    delay.send_keys("45")

    # input in calculator
    driver.find_element(By.XPATH, "//*[text()='7']").click()
    driver.find_element(By.XPATH, "//*[text()='+']").click()
    driver.find_element(By.XPATH, "//*[text()='8']").click()
    driver.find_element(By.XPATH, "//*[text()='=']").click()
    driver.implicitly_wait(4)

    WebDriverWait(driver, 48).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), '15'))

    result = driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
    assert int(result) == 15
