from selenium import webdriver
from Form_ import Form
import allure


@allure.title('Заполнение формы')
@allure.description('Осталось пустое поле zip')
@allure.feature('CREATE')
@allure.severity('critical')
def test_form():
    driver = webdriver.Chrome()
    person = Form(driver)
    with allure.step('Открыть форму'):
        person.open_form()
    with allure.step('Внести заданные значения {list} в поля'):
        list = ['Иван', 'Петров', 'Ленина, 55/3', 'test@skypro.com',
                '+7985899998787', '', 'Москва', 'Россия', 'QA', 'Skypro']
        person.fill_out_the_form(list)
    with allure.step('Проверить правильность отображения цвета фона полей'):
        person.assser_background_color_field()
    driver.quit()
