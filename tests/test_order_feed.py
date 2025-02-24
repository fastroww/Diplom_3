import pytest
import allure
from selenium.webdriver.common.by import By
from locators.order_feed_page_locators import OrderFeedPageLocators

class TestOrderFeed:
    @allure.title("Тест: Проверка кнопки состава заказа")
    def test_order_composition_button(self, order_feed_page):
        with allure.step("Кликаем на первый заказ в ленте"):
            order_feed_page.click_first_order()
        with allure.step("Проверяем, что отображается заголовок 'Состав заказа'"):
            assert order_feed_page.find_visible_element(OrderFeedPageLocators.ORDER_COMPOSITION_TITLE)

    @allure.title("Тест: Проверка отображения заказа пользователя в ленте заказов")
    def test_user_order_in_order_feed(self, order_feed_page, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Перетаскиваем булку в заказ"):
            main_page.drag_bun_to_order()
        with allure.step("Кликаем на кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
        with allure.step("Получаем номер заказа"):
            identifier_order = main_page.get_order_number()
        with allure.step("Закрываем окно заказа"):
            main_page.click_close_identifier_order()
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Проверяем, что заказ отображается в ленте"):
            locator = (By.XPATH, f'//p[text() = "#0{identifier_order}"]')
            assert order_feed_page.find_visible_element(locator)

    @allure.title("Тест: Проверка счетчика выполненных заказов за сегодня")
    def test_counter_completed_today(self, order_feed_page, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Получаем текущее значение счетчика заказов за сегодня"):
            counter_today_before = int(order_feed_page.get_counter_completed_today())
        with allure.step("Переходим в конструктор"):
            order_feed_page.click_constructor_button()
        with allure.step("Перетаскиваем булку в заказ"):
            main_page.drag_bun_to_order()
        with allure.step("Кликаем на кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
        with allure.step("Закрываем окно заказа"):
            main_page.click_close_identifier_order()
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Получаем новое значение счетчика заказов за сегодня"):
            counter_today_after = int(order_feed_page.get_counter_completed_today())
        with allure.step("Проверяем, что счетчик увеличился"):
            assert counter_today_after > counter_today_before

    @allure.title("Тест: Проверка общего счетчика выполненных заказов")
    def test_counter_completed_all(self, order_feed_page, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Получаем текущее значение общего счетчика заказов"):
            counter_all_before = int(order_feed_page.get_counter_completed_all())
        with allure.step("Переходим в конструктор"):
            order_feed_page.click_constructor_button()
        with allure.step("Перетаскиваем булку в заказ"):
            main_page.drag_bun_to_order()
        with allure.step("Кликаем на кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
        with allure.step("Закрываем окно заказа"):
            main_page.click_close_identifier_order()
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Получаем новое значение общего счетчика заказов"):
            counter_all_after = int(order_feed_page.get_counter_completed_all())
        with allure.step("Проверяем, что счетчик увеличился"):
            assert counter_all_after > counter_all_before

    @allure.title("Тест: Проверка отображения заказа в разделе 'В работе'")
    def test_list_order_at_works(self, order_feed_page, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Перетаскиваем булку в заказ"):
            main_page.drag_bun_to_order()
        with allure.step("Кликаем на кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
        with allure.step("Получаем номер заказа"):
            identifier_order = main_page.get_order_number()
        with allure.step("Закрываем окно заказа"):
            main_page.click_close_identifier_order()
        with allure.step("Переходим в ленту заказов"):
            main_page.click_order_feed_button()
        with allure.step("Проверяем, что заказ отображается в разделе 'В работе'"):
            locator = (By.XPATH, f"//li[text() = '{identifier_order}']")
            assert order_feed_page.find_visible_element(locator)