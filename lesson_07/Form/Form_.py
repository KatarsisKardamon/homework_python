from selenium.webdriver.common.by import By


class Form:
    def __init__(self, driver):
        self.driver = driver

    def open_form(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def fill_out_the_form(self, list):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(list[0])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(list[1])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=address"]').send_keys(list[2])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=e-mail"]').send_keys(list[3])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=phone"]').send_keys(list[4])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=zip-code"]').send_keys(list[5])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=city"]').send_keys(list[6])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=country"]').send_keys(list[7])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name=job-position"]').send_keys(list[8])
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(list[9])

        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def assser_background_color_field(self):

        background_color_red = self.driver.find_element(
                By.CSS_SELECTOR, '#zip-code').value_of_css_property(
                      "background-color")
        assert (background_color_red == 'rgba(248, 215, 218, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#last-name').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#address').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#e-mail').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#phone').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#city').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#job-position').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#company').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')

        background_color_green = self.driver.find_element(
                By.CSS_SELECTOR, '#country').value_of_css_property(
                      "background-color")
        assert (background_color_green == 'rgba(209, 231, 221, 1)')
