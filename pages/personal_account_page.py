from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import constants
import allure

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.PERSONAL_ACCOUNT_URL

    @allure.step("Кликаем на кнопку 'История заказов'")
    def click_order_history_button(self):
        self.click(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step("Кликаем на кнопку 'Выйти'")
    def click_logout_button(self):
        self.click(PersonalAccountPageLocators.LOGOUT_BUTTON)