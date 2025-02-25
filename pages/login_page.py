from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import constants
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.LOGIN_URL

    @allure.step("Кликаем на кнопку 'Восстановить пароль'")
    def click_recover_password_button(self):
        self.click(LoginPageLocators.RECOVER_PASSWORD)