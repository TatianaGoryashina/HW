from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class ManePageCalc:
    """
    Этот класс содержит перечень действий,
    необходимых для последовательного выполнения
    домашнего задания "Автоматизация тестирования. Page Object"
    """
    def __init__(self, driver):
        self._driver = driver

    # окрываю сайт
    @allure.title("Открытие калькулятора")
    @allure.description("Запуск браузера и переход на страницу калькулятора")
    @allure.feature("get")
    @allure.step("Открываем калькулятор")
    def open_calc(self):
        """ Открывает сайт калькулятора """
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    # выставляю ожидание для калькулятора
    @allure.title("Выставление ожидания появления результата")
    @allure.description("Настройка ожидания по времени до появления результата"
                        " выполнения действия в калькуляторе")
    @allure.feature("find_element")
    @allure.feature("send_keys")
    @allure.step("Находим поле ввода и вводим значение")
    def wait_resp(self):
        """
        Выставляет ожидание времени
        появления ответа в строке результата на 45 секунд
        """
        with allure.step("Поиск элемента на странице"):
            delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        # delay.clear()
        with allure.step("Очистить поле ввода"):
            delay.send_keys(Keys.BACKSPACE)
        with allure.step("Ввести значение '45' в поле ввода"):
            delay.send_keys("45")

    # совершаю операцию в калькуляторе
    @allure.title("Нажимание кнопок калькулятора")
    @allure.description("Поиск элементов на странице с определенным текстовым "
                        "значением и кликом по нему")
    @allure.feature("find_element")
    @allure.feature("click")
    @allure.step("Находим кнопки и нажимаем")
    def operations(self):
        """
        Отправляет значение цифр для выполнения операции в калькуляторе
        """
        with allure.step("Найти на странице кнопку '7' и кликнуть на нее"):
            self._driver.find_element(By.XPATH, "//*[text()='7']").click()
        with allure.step("Найти на странице кнопку '+' и кликнуть на нее"):
            self._driver.find_element(By.XPATH, "//*[text()='+']").click()
        with allure.step("Найти на странице кнопку '8' и кликнуть на нее"):
            self._driver.find_element(By.XPATH, "//*[text()='8']").click()
        with allure.step("Найти на странице кнопку '=' и кликнуть на нее"):
            self._driver.find_element(By.XPATH, "//*[text()='=']").click()

    # выставление ожидания ответа
    @allure.title("Выставление ожидания для проверки появления элемента")
    @allure.description("Настройка ожидания времени "
                        "поиска появившегося элемента")
    def waiting_resp(self):
        """
        Выставляет ожидание определенного времени ответа
        до появления элемента на странице калькулятора
        """
        with allure.step("Установка ожидания"):
            WebDriverWait(self._driver, 48).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), '15'))

    # сравнение результата
    @allure.title("Проверка результата")
    @allure.description("Сравнение получившегося "
                        "результата калькулятора и заданного значения")
    @allure.feature("find_element")
    def result(self):
        """
        Сравнивает значение появившегося результата
        с тем, которое должно получиться при выполнении сложения
        """
        with allure.step("Проверить, что значение суммы в калькуляторе = 15"):
            result = self._driver.find_element(
                By.CSS_SELECTOR, '[class="screen"]').text
            assert int(result) == 15
