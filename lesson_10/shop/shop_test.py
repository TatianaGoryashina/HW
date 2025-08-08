from selenium import webdriver
import pytest
from shop_page_autorize import autorize
from shop_page_main import main
from shop_page_cart import cart
from shop_page_final import final
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.epic("Проверка итоговой суммы при заказе товара на сайте")
@allure.severity("blocker")
@allure.title("Проверка итоговой суммы и заранее заданного значения")
@allure.description("Выполнение действий на сайте магазина по авторизации, "
                    "выбору товара, переход в корзину, проверка товаров, "
                    "оформление заказа через заполения форм")
def test_shop_buy(driver):
    auto_page = autorize(driver)
    with allure.step("Открыть страницу авторизации"):
        auto_page.open_shop()
    with allure.step("Авторизироваться"):
        auto_page.auto()
    main_page = main(driver)
    with allure.step("Добавить товары в корзину"):
        main_page.add_products()
    with allure.step("Перейти в корзину"):
        main_page.go_to_cart()
    cart_page = cart(driver)
    with allure.step("Нажать кнопку Checkout"):
        cart_page.checkout()
    final_page = final(driver)
    with allure.step("Заполнить поля ввода для оформления заказа"):
        final_page.fill_input_field()
    with allure.step("Сравнить итоговую сумму покупок и заданное значение"):
        final_page.total()
