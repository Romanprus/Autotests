import allure
from selenium.webdriver.common.by import By

from Framework.page_objects.course_page.star_cours_page import StartCourse
from Framework.utilities.web_ui.base_page import BasePage


class CoursePage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __cource_title = (By.XPATH, "//h1[text()='Modern React and NodeJS Development']")
    __play_button = (By.XPATH, '//button[@class="w-big-play-button w-css-reset-button-important w-vulcan-v2-button"]')
    __video_start = (By.XPATH, '//div[@id="w-vulcan-v2-31"]')
    __course_info_section = (By.XPATH, '//button[@aria-controls="chapter-1"]')
    __course_info_lesson1 = (By.XPATH, "//div//p[text()='Introduction']")
    __course_info_section_second_lesson = (By.XPATH, '//button[@aria-controls="chapter-2"]')
    __course_info_lesson2 = (By.XPATH, "//div//p[text()='Start a Server']")
    __hide_button = (
        By.XPATH, "//h3[text()='Coding and testing an authentication API [NodesJs + Cypress]']//..//button")
    __star_course = (By.XPATH, '//div[@class="pricing-table__list-item-details"]//..//a')
    __instructor_email = (By.XPATH, '//*[@class="instructor__email"]')
    __instructor_photo = (By.CSS_SELECTOR, 'div[class="instructor__avatar"]')
    __first_lesson_info = (By.CSS_SELECTOR, "ul#chapter-1")
    __second_lesson_info = (By.CSS_SELECTOR, "ul#chapter-2")

    @allure.step
    def play_video(self):
        self._click(self.__play_button)
        return self

    @allure.step
    def title_value(self):
        element = self._get_value(self.__course_info_lesson1)
        return element

    @allure.step
    def title_value_2(self):
        element = self._get_value(self.__course_info_lesson2)
        return element

    @allure.step
    def is_video_start(self) -> 'bool':
        return self._is_displayed(self.__video_start)

    @allure.step
    def is_title_visible(self) -> 'bool':
        return self._is_displayed(self.__cource_title)

    @allure.step
    def open_info_section(self):
        self._click(self.__course_info_section)
        return self

    @allure.step
    def hide_info_section(self):
        self._click(self.__course_info_section)
        return self

    @allure.step
    def start_course(self):
        self._is_displayed(self.__star_course)
        self._click(self.__star_course)
        return StartCourse(self._driver)

    @allure.step
    def is_email_present(self) -> 'bool':
        return self._is_displayed(self.__instructor_email)

    @allure.step
    def is_photo_displayed(self) -> 'bool':
        return self._is_displayed(self.__instructor_photo)

    @allure.step
    def is_info_list_displayed(self) -> 'bool':
        return self._is_displayed(self.__first_lesson_info)

    @allure.step
    def is_info_list_second_lesson_displayed(self) -> 'bool':
        return self._is_displayed(self.__second_lesson_info)
