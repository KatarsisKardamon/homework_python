from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

field_username = 'input#username'
input_username = driver.find_element(By.CSS_SELECTOR, field_username)

field_password = 'input#password'
input_password = driver.find_element(By.CSS_SELECTOR, field_password)

button_login = "i.fa-sign-in"
click_button = driver.find_element(By.CSS_SELECTOR, button_login)

input_username.send_keys('tomsmith')
input_password.send_keys('SuperSecretPassword!')
click_button.click()

flash_messages = "#flash"
output_messages = driver.find_element(By.CSS_SELECTOR, flash_messages)

print(output_messages.text)
sleep(10)

driver.quit()
