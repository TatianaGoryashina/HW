from selenium.webdriver.common.by import By
import allure


class autorize:
    """
    Этот класс содержит действия для авторизации на сайте
    при выполнении домашнего задания "Автоматизация тестирования. Page Object"
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.title("Страница авторизация")
    @allure.description("Открытие в браузере страницы авторизации")
    @allure.feature("get")
    @allure.step("Открываем страницу авторизации")
    def open_shop(self):
        """
        Открывает страницу авторизации магазина
        """
        # переход на сайт
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)

    @allure.title("Авторизация")
    @allure.description("Введение данных на странице авторизации для перехода"
                        " на страницу выбора товаров")
    @allure.feature("find_element")
    @allure.feature("send_keys")
    @allure.feature("click")
    @allure.step("Находим поля и вводим значения")
    def auto(self):
        """
        Находит поля 'user-name', 'password', вставляет в них значения
        и нажимает на кнопку 'login'
        """
        # авторизация на сайте
        with allure.step("Найти поле ввода имени пользователя и ввести "
                         "значение"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        with allure.step("Найти поле ввода пароля и ввести значение"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        with allure.step("Найти и нажать кнопку 'login'"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-button").click()
