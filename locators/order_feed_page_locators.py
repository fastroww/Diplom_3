from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка "Конструктор"
    FIRST_ORDER = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    ORDER_COMPOSITION_TITLE = (By.XPATH, "//p[text() = 'Cостав']")
    COUNTER_COMPLETED_ALL = (By.CSS_SELECTOR, 'div.OrderFeed_ordersData__1L6Iv > div.undefined.mb-15 > p.OrderFeed_number__2MbrQ.text.text_type_digits-large')
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[contains(., 'Выполнено за сегодня:')]/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    LIST_ORDER_AT_WORK = (By.XPATH, '//ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//li[@class = "text text_type_digits-default mb-2"]')
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, f'//p[@class = "text text_type_digits-default"]')