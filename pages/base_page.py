import time

import pytest
import allure
from selenium.webdriver import ActionChains
from constants import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.url = BASE_URL
        self.action_chains = ActionChains(self.driver)

    @allure.step("Открываем страницу")
    def open_page(self):
        self.driver.get(self.url)

    @allure.step("Ожидаем, что URL содержит: {url}")
    def wait_url_contains(self, url):
        self.wait.until(EC.url_contains(url))

    @allure.step("Ищем элемент по локатору: {locator}")
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Скроллим к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем на элемент по локатору: {locator}")
    def click(self, locator):
        element = self.find_clickable_element(locator)
        self.scroll_to_element(element)
        time.sleep(2)
        element.click()

    @allure.step("Ищем видимый элемент по локатору: {locator}")
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Вводим текст '{text}' в элемент по локатору: {locator}")
    def enter_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст из элемента по локатору: {locator}")
    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text

    @property
    @allure.step("Получаем текущий URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскиваем элемент {locator_to_drag} на элемент {locator_target}")
    def drag_element(self, locator_to_drag, locator_target):
        element_to_drag = self.find_visible_element(locator_to_drag)
        target_element = self.find_visible_element(locator_target)
        self.action_chains.drag_and_drop(element_to_drag, target_element).perform()