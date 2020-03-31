from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
