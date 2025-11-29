from selenium import webdriver
from Authorization_ import Authorization
from AddToCart_ import AddToCart
from Checkout_ import Checkout
from CreateOrder_ import CreateOrder
import allure


@allure.title('Оформление покупки в магазине')
@allure.description('Авторизация standard_user')
@allure.feature('CREATE')
@allure.severity('normal')
def test_shop():
    driver = webdriver.Chrome()

    user = Authorization(driver)
    with allure.step('Открыть сайт магазина'):
        user.open_shop()

    with allure.step(
        'Авторизироваться в магазине под логином {user} и паролем {password}'
    ):
        user.authorization('standard_user', 'secret_sauce')

    with allure.step('Добавить товары {product_id} в корзину'):
        product = AddToCart(driver)

        product.add_to_cart('add-to-cart-sauce-labs-backpack')
        product.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
        product.add_to_cart('add-to-cart-sauce-labs-onesie')

    with allure.step('Перейти в корзину'):
        product.to_cart()

    with allure.step('Проверить заказ'):
        check = Checkout(driver)
        check.checkout()

    with allure.step(
        'Создать заказ с заполнением параметром {first_name},{last_name},{zip}'
    ):
        order = CreateOrder(driver)
        order.create_order('standard_name', 'secret_name', '444555')

    with allure.step('Напечатать счет'):
        order.print_total()

    driver.quit()
