from selenium import webdriver
from Calculator_ import Calculator
import allure


@allure.title('Калькулятор с задержкой')
@allure.description('Вычисление суммы')
@allure.feature('READ')
@allure.severity('critical')
def test_calculator():
    driver = webdriver.Chrome()
    example = Calculator(driver)
    with allure.step('Открыть калькулятор'):
        example.open_calculator()
    with allure.step('Задать задержку {time}'):
        example.set_the_time(2)
    with allure.step('Набрать в калькуляторе заданые значения {a}, {b}'):
        example.calculation_sum(7, 8)
    with allure.step('Сравнить выведенное число с реальным результатом'):
        example.assert_result()
    driver.quit()
