from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")


driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

content = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

txt = content.text

print(txt)

driver.quit()
