from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

field_input = 'input[type="number"]'
input_text = driver.find_element(By.CSS_SELECTOR, field_input)

input_text.send_keys('Sky')
sleep(1)
input_text.clear()
sleep(1)
input_text.send_keys('Pro')
sleep(10)

driver.quit()
