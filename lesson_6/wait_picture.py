from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 20)

# переходим на сайт
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()  # чтобы было видно все появляющиеся картинки

# устанавливаем ожидания
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done"))

# вывод в консоль атрибута
pictures = driver.find_elements(By.CSS_SELECTOR, "img")
srs = pictures[3].get_attribute('src')
print(srs)

driver.quit()
