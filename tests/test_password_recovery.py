import allure
import pytest
import constants

class TestPasswordRecovery:
    @allure.title("Тест: Проверка кнопки 'Восстановить пароль'")
    def test_recover_password_button(self, login_page):
        with allure.step("Кликаем на кнопку 'Восстановить пароль'"):
            login_page.click_recover_password_button()
        with allure.step("Проверяем, что URL соответствует странице восстановления пароля"):
            assert login_page.current_url == constants.PASSWORD_RECOVERY_URL

    @allure.title("Тест: Ввод email и клик на кнопку восстановления")
    def test_input_email_and_click(self, password_recovery_page):
        with allure.step("Вводим email в поле ввода"):
            password_recovery_page.input_email()
        with allure.step("Кликаем на кнопку 'Восстановить'"):
            password_recovery_page.click_recovery_button()
        with allure.step("Ожидаем, что URL содержит 'reset'"):
            password_recovery_page.wait_url_contains("reset")
        with allure.step("Проверяем, что URL соответствует странице сброса пароля"):
            assert password_recovery_page.current_url == constants.RESET_PASSWORD_URL

    @allure.title("Тест: Проверка кнопки 'Показать пароль'")
    def test_show_password_button(self, password_recovery_page):
        with allure.step("Вводим email в поле ввода"):
            password_recovery_page.input_email()
        with allure.step("Кликаем на кнопку 'Восстановить'"):
            password_recovery_page.click_recovery_button()
        with allure.step("Кликаем на кнопку 'Показать пароль'"):
            password_recovery_page.click_show_password()
        with allure.step("Проверяем, что поле ввода пароля активно"):
            assert 'input_status_active' in password_recovery_page.get_show_password().get_attribute('class')