from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()


def test_color_forms(driver):
    # переход на страницу сайта
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)

    # заполняю формы значениями
    driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, '[name="city"]').send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    # нажимаем на кнопку
    driver.find_element(
        By.CSS_SELECTOR, '[type="submit"]').click()

    # создаю переменные для проверки
    first_name = driver.find_element(
        By.CSS_SELECTOR, '[id="first-name"]')
    last_name = driver.find_element(
        By.CSS_SELECTOR, '[id="last-name"]')
    adress = driver.find_element(
        By.CSS_SELECTOR, '[id="address"]')
    city = driver.find_element(
        By.CSS_SELECTOR, '[id="city"]')
    country = driver.find_element(
        By.CSS_SELECTOR, '[id="country"]')
    email = driver.find_element(
        By.CSS_SELECTOR, '[id="e-mail"]')
    phone = driver.find_element(
        By.CSS_SELECTOR, '[id="phone"]')
    job_position = driver.find_element(
        By.CSS_SELECTOR, '[id="job-position"]')
    company = driver.find_element(
        By.CSS_SELECTOR, '[id="company"]')

    # проверка поля zip code
    zip_code_style = driver.find_element(By.ID, "zip-code")
    assert zip_code_style.get_attribute("class") == "alert py-2 alert-danger"

    # проверка остальных полей
    forms = [
        first_name,
        last_name,
        adress,
        city,
        country,
        email,
        phone,
        job_position,
        company
        ]
    for form in forms:
        assert form.get_attribute(
            "class") == "alert py-2 alert-success"
