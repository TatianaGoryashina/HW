from selenium.webdriver.common.by import By


class autorize:
    def __init__(self, driver):
        self.driver = driver

    def open_shop(self):
        # переход на сайт
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)

    def auto(self):
        # авторизация на сайте
        self.driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()
