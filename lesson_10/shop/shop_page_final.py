from selenium.webdriver.common.by import By
import allure


class final:
    """
    Этот класс описывает заполнение полей данных для оформления заказа
    при выполнении домашнего задания "Автоматизация тестирования. Page Object"
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.title("Оформление заказа")
    @allure.description("Заполнение форм ввода для оформления заказа")
    @allure.feature("find_element")
    @allure.feature("send_keys")
    @allure.feature("click")
    @allure.step("Находим поля ввода, вводим в них значения и нажимаем кнопку "
                 "'Continue'")
    def fill_input_field(self):
        """
        Находит поля ввода и отправляет в них значения,
        находит кнопку 'continue' и нажимает её
        """
        # Запонение полей ввода данных пользователя
        with allure.step("Нахожу поле ввода имени и ввожу значение"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#first-name").send_keys("Tatiana")
        with allure.step("Нахожу поле ввода фамилии и ввожу значение"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#last-name").send_keys("Goryashina")
        with allure.step("Нахожу поле ввода индекса и ввожу значение"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#postal-code").send_keys("670045")
        with allure.step("Нахожу кнопку 'Continue' и нажимаю её"):
            # нажимаю продолжить
            self.driver.find_element(
                By.CSS_SELECTOR, "#continue").click()

    @allure.title("Сравнение итогого значения и заданного значения")
    @allure.description("Сравение итоговой суммы заказа и "
                        "заранее предустановленного значения")
    @allure.feature("find_element")
    @allure.step("Сравниваем итоговую сумму и 'Total: $58.29'")
    def total(self):
        """
        Находит значение total на странице,
        сравнивает значение total и предустановленное значение
        """
        # прочесть total
        txt = self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="total-label"]').text
        # сравнение значения total
        assert txt == "Total: $58.29"
