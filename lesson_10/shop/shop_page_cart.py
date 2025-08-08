from selenium.webdriver.common.by import By
import allure


class cart:
    """
    Этот класс описывает взаимодействие с корзиной магазина
    при выполнении домашнего задания "Автоматизация тестирования. Page Object"
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.title("Кнопка Checkout")
    @allure.description("Нажатие на кнопку Checkout")
    @allure.feature("find_element")
    @allure.feature("click")
    @allure.step("Находим и нажимаем кнопку Checkout")
    def checkout(self):
        """
        Находит и нажимает кнопку 'checkout'
        """
        # chekout
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
