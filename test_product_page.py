from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


# Константа ссылки
main_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    product_page.should_be_actual_price()


@pytest.mark.parametrize("link", [pytest.param(main_link, marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize("link", [main_link])
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize("link", [pytest.param(main_link, marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


@pytest.mark.login_guest
class TestLoginFromProductPage():
    @pytest.mark.parametrize("link", [main_link])
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link", [main_link])
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize("link", [main_link])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize("link", [main_link])
    def test_user_cant_see_success_message(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize("link", [main_link])
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_be_success_message()
        product_page.should_be_actual_price()
