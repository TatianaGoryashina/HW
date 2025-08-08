from selenium.webdriver.common.by import By
import allure


class main:
    """
    Этот класс описывает взаимодействие с товарами магазина
    при выполнении домашнего задания "Автоматизация тестирования. Page Object"
    """
    def __init__(self, driver):
        self.driver = driver

    @allure.title("Добавление товаров в корзину")
    @allure.description("Поиск товаров и добавление их в корзину")
    @allure.feature("find_element")
    @allure.feature("click")
    @allure.step("Находим определенные товары и добавляем их в корзину")
    def add_products(self):
        """
        Ищет товары на странице и добавление их в корзину
        """
        # добавление товаров в корзину
        with allure.step("Нахожу первый товар и нажимаю добавить"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        with allure.step("Нахожу второй товар и нажимаю добавить"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
            ).click()
        with allure.step("Нахожу третий товар и нажимаю добавить"):
            self.driver.find_element(
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.title("Переход в корзину")
    @allure.description("Перейти на страницу корзины")
    @allure.feature("find_element")
    @allure.feature("click")
    @allure.step("Находим кнопку перехода в корзину и нажимаем на нее")
    def go_to_cart(self):
        """
        Находит кнопку для перехода в корзину и нажимает её
        """
        # перейти в корзину
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
        # or driver.get("https://www.saucedemo.com/cart.html")
