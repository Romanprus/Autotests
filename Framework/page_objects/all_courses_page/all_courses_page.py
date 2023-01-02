import allure
from selenium.webdriver.common.by import By

from Framework.page_objects.course_page.course_page import CoursePage
from Framework.utilities.web_ui.base_page import BasePage


class AllCourses(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __user_avatar = (By.XPATH, "//img[@class='header__user-avatar']")
    __search_field = (By.XPATH, '//label//input[@name="q"]')  # only after login
    __second_page = (By.XPATH, "//li/a[text()='2']")
    __collections = (By.CSS_SELECTOR, 'section[class="header__logo header__logo___2909e"]')
    __previous_page_button = (By.XPATH, '//li//i[@class="fa fa-chevron-left"]')
    __next_page_button = (By.XPATH, '//*[@aria-label="Next page"]')
    __course_item = (By.CSS_SELECTOR, 'div a[href="/courses/react-and-nodejs"]')
    __drop_down_menu = (By.XPATH, '//li[class="dropdown header__nav-item"]')  # appears after login
    __logout_button = (
        By.CSS_SELECTOR, 'ul[class="dropdown__menu"]:last-child a[href="/users/sign_out"]')  # appears after login
    __search_title = (By.CSS_SELECTOR, 'h2[class="products__title"]')  # only after seach
    __more_courses = (By.XPATH, "//section//a[text()='View more courses']")  # button appears only before login
    __first_title = (By.XPATH, "//header/h2[text()='Worldclass Automation Training']")

    @allure.step
    def is_user_avatar_visible(self) -> 'bool':
        return self._is_displayed(self.__user_avatar)

    @allure.step
    def enter_something_in_search(self, text=str):
        self._send_keys(self.__search_field, text)
        return self

    @allure.step
    def press_enter(self):
        self._send_enter(self.__search_field)
        return self

    @allure.step
    def choose_course(self):
        self._click(self.__course_item)
        return CoursePage(self._driver)

    @allure.step
    def next_page(self):
        self._click(self.__next_page_button)
        return self

    @allure.step
    def previous_page(self):
        self._click(self.__previous_page_button)
        return self

    @allure.step
    def click_drop_down(self):
        self._click(self.__drop_down_menu)
        return self

    @allure.step
    def logout(self):
        self._click(self.__logout_button)
        return AllCourses(self._driver)

    @allure.step
    def click_on_search(self):
        self._click(self.__search_field)
        return self

    @allure.step
    def is_search_title_visible(self) -> 'bool':
        return self._is_displayed(self.__search_title)

    @allure.step
    def choose_page(self):
        self._click(self.__second_page)
        return self

    @allure.step
    def is_first_course_invisible(self) -> 'bool':
        return self._is_invisible(self.__course_item)

    @allure.step
    def open_collections(self):
        self._click(self.__collections)
        return self

    @allure.step
    def open_more_courses(self):
        self._click(self.__more_courses)
        return self

    @allure.step
    def is_main_title_displayed(self) -> 'bool':
        return self._is_displayed(self.__first_title)
