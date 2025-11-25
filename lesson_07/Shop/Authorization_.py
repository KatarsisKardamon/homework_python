from selenium.webdriver.common.by import By


class Authorization:
    def __init__(self, driver):
        self.driver = driver

    def open_shop(self):
        self.driver.get("https://www.saucedemo.com")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def authorization(self, user, password):
        self.user = user
        self.password = password
        self.driver.find_element(
            By.CSS_SELECTOR, '#user-name').send_keys(self.user)
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys(self.password)
        self.driver.find_element(
            By.CSS_SELECTOR, '#login-button').click()
