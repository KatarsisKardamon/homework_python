from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys(2)
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-outline-warning").click()

    wait = WebDriverWait(driver, 60)
    result_element = wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
    result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
    result_text = result_element.text.strip()

    assert result_text == "15"

    driver.quit()

test_calculator()
