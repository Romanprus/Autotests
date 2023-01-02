import allure
from selenium.webdriver.common.by import By

from Framework.utilities.web_ui.base_page import BasePage


class StartCourse(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __start_title = (By.CSS_SELECTOR, "div[class='product-title cart-info__title']")

    @allure.step
    def is_course_name_displayed(self) -> 'bool':
        return self._is_displayed(self.__start_title)
