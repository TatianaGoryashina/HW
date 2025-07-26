from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from mane_page_calc import ManePageCalc
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_waiter_calc(driver):
    mane_page_calc = ManePageCalc(driver)
    mane_page_calc.open_calc()
    mane_page_calc.wait_resp()
    mane_page_calc.operations()
    mane_page_calc.waiting_resp()
    mane_page_calc.result()
