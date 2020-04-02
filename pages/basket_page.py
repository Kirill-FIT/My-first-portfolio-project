from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_not_be_basket_items(self): # элементы корзины представлены, но не должны быть
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be."
    def should_be_message_basket_is_empty(self): # сообщение о том, что корзина пуста представлено
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "A message that the basket is empty is not presented."
