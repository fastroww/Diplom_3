from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import constants
import allure

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.PASSWORD_RECOVERY_URL

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_recovery_button(self):
        self.click(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step("Вводим email в поле ввода")
    def input_email(self):
        self.enter_text(PasswordRecoveryPageLocators.EMAIL_INPUT, constants.EMAIL)

    @allure.step("Кликаем на кнопку 'Показать пароль'")
    def click_show_password(self):
        self.click(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Получаем элемент поля ввода пароля")
    def get_show_password(self):
        return self.driver.find_element(*PasswordRecoveryPageLocators.PASSWORD_FIELD)