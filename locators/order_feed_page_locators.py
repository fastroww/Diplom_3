from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка "Конструктор"
    FIRST_ORDER = (By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6']/a[1]")
    ORDER_COMPOSITION_TITLE = (By.XPATH, "//p[text() = 'Cостав']")
    COUNTER_COMPLETED_ALL = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[2]/p[2]')
    COUNTER_COMPLETED_TODAY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]')
    LIST_ORDER_AT_WORK = (By.XPATH, "//li[@class = 'text text_type_main-small']")