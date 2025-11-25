from selenium import webdriver
from Authorization_ import Authorization
from AddToCart_ import AddToCart
from Checkout_ import Checkout
from CreateOrder_ import CreateOrder


def test_shop():
    driver = webdriver.Chrome()

    user = Authorization(driver)

    user.open_shop()

    user.authorization('standard_user', 'secret_sauce')

    product = AddToCart(driver)

    product.add_to_cart('add-to-cart-sauce-labs-backpack')
    product.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    product.add_to_cart('add-to-cart-sauce-labs-onesie')

    product.to_cart()

    check = Checkout(driver)
    check.checkout()

    order = CreateOrder(driver)
    order.create_order('standard_name', 'secret_name', '444555')

    order.print_total()


test_shop()
