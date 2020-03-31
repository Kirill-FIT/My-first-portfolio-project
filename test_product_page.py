from selenium import webdriver
from .pages.product_page import ProductPage
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

"""veb_sites = [
    ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"),
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8"),
    # ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9")
]

@pytest.mark.parametrize('page', veb_sites)
class TestPage(object):
    def test_guest_can_add_product_to_basket(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        # page.should_be_promo_in_the_url()
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
        
    def test_guest_cant_see_success_message(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_message_disappeared_after_adding_product_to_basket(self, browser, page):
        link = f"{page}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_be_success_message_is_disappeared()"""

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
        
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
