from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"].btn-primary')

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner")
