from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )

my_cookie = { #название переменной придумываем сами, открываем скобки
	'name': 'cookie_policy', #ключ
	'value': '1'} #значение, закрываем скобки

browser.get("https://www.labirint.ru/")
browser.add_cookie(my_cookie)

browser.refresh()

sleep(10)
browser.quit()
