from selenium import webdriver
from lesson_07.Calculator.Calculator_ import Calculator


def test_calculator():
    driver = webdriver.Chrome()
    example = Calculator(driver)

    example.open_calculator()

    example.set_the_time(2)

    example.calculation_sum(7, 8)

    example.assert_result()


test_calculator()
