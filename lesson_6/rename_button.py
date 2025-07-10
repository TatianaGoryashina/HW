from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# устанавливаем ожидания
driver.implicitly_wait(4)

# переходим на сайт
driver.get("http://uitestingplayground.com/textinput")

# работа с полем ввода
my_button = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
my_button.click()
my_button.send_keys("SkyPro")

# нажатие синей кнопки
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# вывод текста в консоль
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

driver.quit()
