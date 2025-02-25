from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    RECOVERY_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    INACTIVE_FIELD = (By.XPATH, '//div[@class = "input pr-6 pl-6 input_type_password input_size_default input_status_active"]')
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'div.input_status_active')
