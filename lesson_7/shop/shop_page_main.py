from selenium.webdriver.common.by import By


class main:
    def __init__(self, driver):
        self.driver = driver

    def add_products(self):
        # добавление товаров в корзину
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        # перейти в корзину
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
        # or driver.get("https://www.saucedemo.com/cart.html")
