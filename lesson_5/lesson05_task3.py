from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver: webdriver.Firefox = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Sky")
sleep(1)

input_field.clear()
sleep(1)

input_field.send_keys("Pro")
sleep(1)

driver.quit()
