from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет"
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href = '/feed']")
    BUN_TITLE = (By.XPATH, "//h2[text() = 'Булки']")  # Заголовок "Булки"
    FLUR_BUN = (By.XPATH, "//img[@alt = 'Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "// h2[text() = 'Детали ингредиента']")
    CLOSE_INGREDIENT_BUTTON = (By.XPATH, '//div[@class="Modal_modal__container__Wo2l_"]/button[1]')
    ORDER_FIELD = (By.XPATH, "//span[text() = 'Перетяните булочку сюда (верх)']")
    COUNTER_BUN = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p')
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    ORDER_COOKING_TITLE = (By.XPATH, "//p[text()= 'Ваш заказ начали готовить']")
    ORDER_NUMBER = (By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    CLOSE_IDENTIFIER_ORDER_BUTTON = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
