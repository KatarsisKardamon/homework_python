from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver

    def open_calculator(self):
        self.driver.get(r"https://bonigarcia.dev/selenium-"
                        r"webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_the_time(self, time):
        self.time = time
        delay = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(time)

    def calculation_sum(self, a, b):
        self.sum = a + b
        self.driver.find_element(By.XPATH,
                                 f"//span[text()='{a}']").click()
        self.driver.find_element(By.XPATH,
                                 "//span[text()='+']").click()
        self.driver.find_element(By.XPATH,
                                 f"//span[text()='{b}']").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".btn-outline-warning").click()

    def assert_result(self):
        wait = WebDriverWait(self.driver, 60)
        result_element = wait.until(
                    EC.text_to_be_present_in_element(
                        (By.CSS_SELECTOR, ".screen"), f"{self.sum}")
                )
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        result_text = result_element.text.strip()
        assert result_text == f"{self.sum}"
