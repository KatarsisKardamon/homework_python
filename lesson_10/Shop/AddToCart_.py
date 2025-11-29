from selenium.webdriver.common.by import By


class AddToCart:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        self.product_id = product_id
        self.driver.find_element(
            By.CSS_SELECTOR, f'#{self.product_id}').click()

    def to_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
