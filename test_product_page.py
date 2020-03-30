from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_in_the_url()
    page.should_be_button_add_product_to_basket()
    page.push_button_add_product_to_basket()
    page.should_be_quiz()
    page.should_be_name_equal()
    page.should_be_prise_equal()
