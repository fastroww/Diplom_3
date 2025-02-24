from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    ORDER_HISTORY = (By.XPATH, '//a[text() = "История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка "Выход"