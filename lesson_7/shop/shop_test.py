from selenium import webdriver
import pytest
from shop_page_autorize import autorize
from shop_page_main import main
from shop_page_cart import cart
from shop_page_final import final


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_buy(driver):
    auto_page = autorize(driver)
    auto_page.open_shop()
    auto_page.auto()
    main_page = main(driver)
    main_page.add_products()
    main_page.go_to_cart()
    cart_page = cart(driver)
    cart_page.checkout()
    final_page = final(driver)
    final_page.fill_input_field()
    final_page.total()
