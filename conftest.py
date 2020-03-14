import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options                        # Объявление нужного языка для Chrome

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",     # Браузером по умолчанию является Chrome. Для предоставления выбора браузера указывается код default=None.
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",             # Языком по умолчанию является En. Для предоставления выбора языка указывается код default=None. 
                     help="Choose language: ru, en or ..")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = Options()                                                  # Объявление нужного языка для Chrome
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()                                      # Объявление нужного языка для Firefox 
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



    
"""
Чтобы указать язык браузера с помощью WebDriver, используется класс Options и метод add_experimental_option.
Для Firefox объявление нужного языка будет выглядеть немного иначе.
"""