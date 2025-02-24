import pytest
import requests
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage
from helpers import generate_user_data
import constants
from locators.login_page_locators import LoginPageLocators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    else:
        raise ValueError('Unknown browser type')
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_page()
    return page

@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    page.open_page()
    return page

@pytest.fixture
def password_recovery_page(driver):
    page = PasswordRecoveryPage(driver)
    page.open_page()
    return page

@pytest.fixture
def personal_account_page(driver):
    page = PersonalAccountPage(driver)
    page.open_page()
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_page()
    return page

@pytest.fixture(scope="function")
def create_and_delete_user():
    """
    Фикстура для создания и удаления пользователя.
    """
    payload = generate_user_data()
    response = requests.post(constants.BASE_URL + constants.CREATE_USER, json=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(constants.BASE_URL + constants.DELETE_USER, headers={'Authorization': access_token})

@pytest.fixture(scope="function")
def login_user(login_page):
    def _login_user(create_and_delete_user):
        response, payload = create_and_delete_user
        email = payload['email']
        password = payload['password']
        login_page.enter_text(LoginPageLocators.EMAIL_INPUT_LOGIN, email)
        login_page.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        login_page.click(LoginPageLocators.BUTTON_LOGIN)
    return _login_user
