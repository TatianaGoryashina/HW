from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver: webdriver.Firefox = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
sleep(2)

message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(message.text)

driver.quit()
