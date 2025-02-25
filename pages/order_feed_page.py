from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
import constants
import allure

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.ORDER_FEED_URL

    @allure.step("Кликаем на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликаем на первый заказ в ленте")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step("Получаем количество выполненных заказов за сегодня")
    def get_counter_completed_today(self):
        return self.get_text(OrderFeedPageLocators.COUNTER_COMPLETED_TODAY)

    @allure.step("Получаем общее количество выполненных заказов")
    def get_counter_completed_all(self):
        return self.get_text(OrderFeedPageLocators.COUNTER_COMPLETED_ALL)

    def get_order_number_in_history(self):
        text = self.get_text(OrderFeedPageLocators.ORDER_NUMBER_IN_HISTORY)
        return text

    def wait_order_number_at_work(self, identifier_order):
        return self.wait.until(
            lambda driver: f'{identifier_order}' in self.get_text(OrderFeedPageLocators.LIST_ORDER_AT_WORK)
        )

    def get_order_number_at_work(self):
        text = self.get_text(OrderFeedPageLocators.LIST_ORDER_AT_WORK)
        return text

    def check_order_composition_title(self):
        text = self.find_visible_element(OrderFeedPageLocators.ORDER_COMPOSITION_TITLE).text
        assert text == 'Cостав'