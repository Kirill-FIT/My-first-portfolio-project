from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage               # Переходы между страницами. Первый способ: возвращать нужный Page Object.
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    """
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    """
    """
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
    """
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    # Переходы между страницами:
    """Первый способ: возвращать нужный Page Object.
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    """
    # Второй подход: переход происходит неявно, страницу инициализируем в теле теста:
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
