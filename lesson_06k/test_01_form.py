from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Edge()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, '[name="first-'
                        f'name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, '[name="last-'
                        f'name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"e-mail"]').send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"phone"]').send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"zip-code"]').send_keys('')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, '[name='
                        f'"company"]').send_keys('SkyPro')

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    background_color_red = driver.find_element(
        By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
    assert (background_color_red == 'rgba(248, 215, 218, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#address').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#company').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    background_color_green = driver.find_element(
        By.CSS_SELECTOR, '#country').value_of_css_property("background-color")
    assert (background_color_green == 'rgba(209, 231, 221, 1)')

    driver.quit()
test_form()