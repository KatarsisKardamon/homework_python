from selenium import webdriver
from lesson_07.Form.Form_ import Form


def test_form():
    driver = webdriver.Chrome()
    person = Form(driver)

    person.open_form()

    list = ['Иван', 'Петров', 'Ленина, 55/3', 'test@skypro.com',
            '+7985899998787', '', 'Москва', 'Россия', 'QA', 'Skypro']
    person.fill_out_the_form(list)

    person.assser_background_color_field()


test_form()
