from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from mane_page_calc import ManePageCalc
import pytest
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.epic("Проверка калькулятора")
@allure.severity("blocker")
@allure.title("Проверка появления ответа в калькуляторе")
@allure.description("На странице калькулятора нужно установить время ожидания "
                    "ответа, ввести значение в калькулятор и, после появления "
                    "результата выполнения операции, сравнить значение "
                    "результата и установленное значение")
def test_waiter_calc(driver):
    mane_page_calc = ManePageCalc(driver)
    with allure.step("Открыть калькулятор"):
        mane_page_calc.open_calc()
    with allure.step("Установить ожидание появления результата"):
        mane_page_calc.wait_resp()
    with allure.step("Выполнить операцию в калькуляторе"):
        mane_page_calc.operations()
    with allure.step("Установить ожидание для поиска элемента на странице"):
        mane_page_calc.waiting_resp()
    with allure.step("Сравнение результата выполнения в калькуляторе"
                     " и заданного значения"):
        mane_page_calc.result()
