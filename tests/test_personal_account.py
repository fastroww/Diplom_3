import pytest
import allure
import constants

class TestPersonalAccount:
    @allure.title("Тест: Проверка кнопки 'Личный кабинет'")
    def test_personal_account_button(self, main_page, login_user, create_and_delete_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Кликаем на кнопку 'Личный кабинет'"):
            main_page.click_personal_account_button()
        with allure.step("Ожидаем, что URL содержит '/account/profile'"):
            main_page.wait_url_contains('/account/profile')
        with allure.step("Проверяем, что текущий URL соответствует странице личного кабинета"):
            assert main_page.current_url == constants.PERSONAL_ACCOUNT_URL

    @allure.title("Тест: Проверка кнопки 'История заказов'")
    def test_order_history_button(self, create_and_delete_user, personal_account_page, main_page, login_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Кликаем на кнопку 'Личный кабинет'"):
            main_page.click_personal_account_button()
        with allure.step("Кликаем на кнопку 'История заказов'"):
            personal_account_page.click_order_history_button()
        with allure.step("Ожидаем, что URL содержит '/account/order-history'"):
            personal_account_page.wait_url_contains("/account/order-history")
        with allure.step("Проверяем, что текущий URL содержит '/account/order-history'"):
            assert "/account/order-history" in personal_account_page.current_url

    @allure.title("Тест: Проверка кнопки 'Выйти'")
    def test_logout_button(self, create_and_delete_user, personal_account_page, main_page, login_user):
        with allure.step("Логиним пользователя"):
            login_user(create_and_delete_user)
        with allure.step("Кликаем на кнопку 'Личный кабинет'"):
            main_page.click_personal_account_button()
        with allure.step("Кликаем на кнопку 'Выйти'"):
            personal_account_page.click_logout_button()
        with allure.step("Ожидаем, что URL содержит '/login'"):
            personal_account_page.wait_url_contains("/login")
        with allure.step("Проверяем, что текущий URL соответствует странице логина"):
            assert constants.LOGIN_URL == personal_account_page.current_url