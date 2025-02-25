from selenium.webdriver.common.by import By

class LoginPageLocators:
    RECOVER_PASSWORD = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    EMAIL_INPUT_LOGIN = (By.XPATH, "//input[@name = 'name']")  # Поле для ввода email в форме для входа
    PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']")  # Поле для ввода пароля
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка "Войти" в форме для входа
