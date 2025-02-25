from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Кликаем на кнопку 'Личный кабинет'")
    def click_personal_account_button(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликаем на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем на булку 'Флюоресцентная булка'")
    def click_flur_bun(self):
        self.click(MainPageLocators.FLUR_BUN)

    @allure.step("Кликаем на кнопку закрытия окна ингредиента")
    def click_close_ingredient_button(self):
        self.click(MainPageLocators.CLOSE_INGREDIENT_BUTTON)

    @allure.step("Перетаскиваем булку в поле заказа")
    def drag_bun_to_order(self):
        self.drag_element(MainPageLocators.FLUR_BUN, MainPageLocators.ORDER_FIELD)

    @allure.step("Получаем значение счетчика булок")
    def get_counter_bun(self):
        return self.get_text(MainPageLocators.COUNTER_BUN)

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_place_order_button(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        order_id = self.get_text(MainPageLocators.ORDER_NUMBER)
        while order_id == '9999':
            order_id = self.get_text(MainPageLocators.ORDER_NUMBER)
        return f"{order_id}"

    @allure.step("Кликаем на кнопку закрытия окна заказа")
    def click_close_identifier_order(self):
        self.click(MainPageLocators.CLOSE_IDENTIFIER_ORDER_BUTTON)

    @allure.step('Проверить закрытие деталей ингредиента')
    def check_close_details(self):
        class_to_check = self.get_class(MainPageLocators.MODAL_WINDOW)
        assert 'Modal_modal_opened__3ISw4' not in class_to_check

    def wait_order_cooking_title(self):
        return self.find_visible_element(MainPageLocators.ORDER_COOKING_TITLE)

    def check_order_cooking_title(self):
        text = self.find_visible_element(MainPageLocators.ORDER_COOKING_TITLE).text
        assert text == 'Ваш заказ начали готовить'

    def wait_normal_order_number(self):
        # Ожидаем, пока номер заказа не станет отличным от '9999'
        return self.wait.until(
            lambda driver: self.get_text(MainPageLocators.ORDER_NUMBER) != '9999'
        )

