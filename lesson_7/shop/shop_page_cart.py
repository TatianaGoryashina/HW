from selenium.webdriver.common.by import By


class cart:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        # chekout
        self.driver.find_element(
            By.CSS_SELECTOR, "#checkout").click()
