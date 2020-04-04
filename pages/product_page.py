from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_promo_in_the_url(self):
        assert "promo=newYear" in self.browser.current_url, "It is not promo page"
    def should_be_button_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button add is not presented."
    def push_button_add_product_to_basket(self):
        button_add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add_product_to_basket.click()
    def should_be_quiz(self):
        self.solve_quiz_and_get_code()
        
    def should_not_be_success_message(self): # сообщение об успехе представлено, но не должно быть
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."
    def should_be_success_message_is_disappeared(self): # сообщение об успехе представлено, но должно исчезнуть
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should is disappeared."    
        
    def should_be_name_equal(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), ('Success message is not present')
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        in_message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == in_message_name, f'"{product_name}" is not "{in_message_name}"'
    def should_be_prise_equal(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), ('Total cost message is not ptesent')
        product_prise = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_prise == basket_cost, f'"{product_prise}" is not "{basket_cost}"'
