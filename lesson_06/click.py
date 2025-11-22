from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-primary")))

content = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

txt = content.text

print(txt)

driver.quit()
