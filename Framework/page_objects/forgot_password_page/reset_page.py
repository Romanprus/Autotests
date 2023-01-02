import allure
from selenium.webdriver.common.by import By

from Framework.utilities.web_ui.base_page import BasePage


class ResetPage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __success_reset_screen = (By.XPATH, "//*[text()='Help is on the way!']")
    __sign_in = (By.XPATH, "//div[@class='header__wrapper']//a[@href='/users/sign_in']")
    __enter_button = (By.XPATH, "//div//input[@value='Sign in']")

    @allure.step
    def is_sucssess_title_displayed(self) -> 'bool':
        return self._is_displayed(self.__success_reset_screen)

    @allure.step
    def title_value(self):
        element = self._get_value(self.__success_reset_screen)
        return element

    @allure.step
    def back_to_sign_in_screen(self):
        self._click(self.__sign_in)
        return self

    @allure.step
    def is_sign_in_button_displayed(self) -> 'bool':
        return self._is_displayed(self.__enter_button)
