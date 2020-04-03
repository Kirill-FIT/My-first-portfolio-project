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
        page.should_be_success_message_is_disappeared()

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

    def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_not_be_basket_items()
        page.should_be_message_basket_is_empty()
"""

@pytest.mark.webtest # маркер webtest зарегистрировал в pytest.ini
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org" # генерация email c использованием текущего времени
        password = str(time.time()) + "fakepa$$word" # генерация password c использованием текущего времени
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
        
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_button_add_product_to_basket()
        page.push_button_add_product_to_basket()
        page.should_be_quiz()
        page.should_be_name_equal()
        page.should_be_prise_equal()


""" Создание объектов по API.
Cоздание нового товара в нашем интернет-магазине перед тестом и удаление по завершении теста:
@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста
"""