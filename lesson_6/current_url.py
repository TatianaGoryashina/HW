from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )

browser.get("http://ya.ru/")
url = browser.current_url
print(url)

browser.quit()
