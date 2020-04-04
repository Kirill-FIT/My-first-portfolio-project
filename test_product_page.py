from selenium import webdriver
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

veb_sites = [
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"),
    ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"),
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9")
]

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_in_the_url()
    page.should_be_button_add_product_to_basket()
    page.push_button_add_product_to_basket()
    page.should_be_quiz()
    page.should_be_name_equal()
    page.should_be_prise_equal()

@pytest.mark.parametrize('page', veb_sites)
class TestPage(object):
    def test_guest_should_see_login_link_on_product_page(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_success_message(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, page):
        link = f"{page}"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_not_be_basket_items()
        page.should_be_message_basket_is_empty()
        
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_be_name_equal()
        page.should_be_prise_equal()

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_not_be_success_message()
        
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_message_disappeared_after_adding_product_to_basket(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_be_success_message_is_disappeared()

@pytest.mark.webtest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakepa$$word"
        login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_be_name_equal()
        page.should_be_prise_equal()
