from selenium.webdriver.common.by import By


class CreateOrder:
    def __init__(self, driver):
        self.driver = driver

    def create_order(self, first_name, last_name, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.zip = zip
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(zip)

        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def print_total(self):
        self.total = self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
        print(self.total)
