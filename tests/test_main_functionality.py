import allure
import pytest
import constants

class TestMainFunctionality:
    @allure.title("Тест: Проверка кнопки 'Конструктор'")
    def test_constructor_button(self, order_feed_page, main_page):
        with allure.step("Кликаем на кнопку 'Конструктор'"):
            order_feed_page.click_constructor_button()
        with allure.step("Проверяем текущий URL"):
            assert main_page.current_url == constants.BASE_URL + "/"

    @allure.title("Тест: Проверка кнопки 'Лента заказов'")
    def test_order_feed_button(self, main_page, order_feed_page):
        with allure.step("Кликаем на кнопку 'Лента заказов'"):
            main_page.click_order_feed_button()
        with allure.step("Ожидаем, что URL содержит '/feed'"):
            order_feed_page.wait_url_contains("/feed")
        with allure.step("Проверяем текущий URL"):
            assert order_feed_page.current_url == constants.ORDER_FEED_URL

    @allure.title("Тест: Проверка деталей ингредиента")
    def test_ingredient_details(self, main_page):
        with allure.step("Кликаем на булку 'Флюоресцентная булка'"):
            main_page.click_flur_bun()
        with allure.step("Проверяем текущий URL"):
            assert main_page.current_url == constants.INGREDIENT_URL

    @allure.title("Тест: Проверка кнопки закрытия окна ингредиента")
    def test_close_ingredient_button(self, main_page):
        with allure.step("Кликаем на булку 'Флюоресцентная булка'"):
            main_page.click_flur_bun()
        with allure.step("Кликаем на кнопку закрытия окна ингредиента"):
            main_page.click_close_ingredient_button()
        with allure.step('Проверить закрытие деталей ингредиента'):
            main_page.check_close_details()

    @allure.title("Тест: Перетаскивание булки в заказ")
    def test_drag_bun_to_order(self, main_page):
        with allure.step("Перетаскиваем булку в поле заказа"):
            main_page.drag_bun_to_order()
        with allure.step("Проверяем, что счетчик булок равен '2'"):
            assert main_page.get_counter_bun() == "2"

    @allure.title("Тест: Оформление заказа")
    def test_place_an_order(self, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Кликаем на кнопку 'Оформить заказ'"):
            main_page.click_place_order_button()
        with allure.step("Перетаскиваем булку в поле заказа"):
            main_page.drag_bun_to_order()
        with allure.step("Ожидаем, что отображается заголовок 'Заказ готовится'"):
            main_page.wait_order_cooking_title()
        with allure.step("Проверяем, что отображается заголовок 'Заказ готовится'"):
            main_page.check_order_cooking_title()