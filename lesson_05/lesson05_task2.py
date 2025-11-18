from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path=r'C:\QA\python\homework_python_02' +
                  r'\homework_python\lesson_05\chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("http://uitestingplayground.com/dynamicid")

blue_button = ".btn-primary"
click_button = driver.find_element(By.CSS_SELECTOR, blue_button)

click_button.click()
sleep(10)

driver.quit()
