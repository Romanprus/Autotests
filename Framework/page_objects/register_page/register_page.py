import allure
from selenium.webdriver.common.by import By

from Framework.utilities.web_ui.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        self._driver = driver
        super().__init__(driver)

    __title = (By.XPATH, '//article[@id="create-account"]//h2')
    __first_name = (By.XPATH, "//input[@id='user[first_name]']")
    __last_name = (By.XPATH, '//input[@id="user[last_name]"]')
    __email = (By.XPATH, '//input[@id="user[email]"]')
    __password = (By.XPATH, '//input[@id="user[password]"]')
    __terms_check_box = (By.CSS_SELECTOR, 'div input[id="user[terms]"]')
    __terms_link = (By.XPATH, "//label//a[text()='Terms of Use']")
    __sign_up_button = (By.CSS_SELECTOR, 'div button[data-callback="onSubmit"]')
    __have_acc_link = (By.XPATH, "//aside//a[text()]")
    __sign_in_link = (By.CSS_SELECTOR, "section ul:last-child li:last-child a")
    __user_avatar = (By.XPATH, "//img[@class='header__user-avatar']")
    __terms_page = (By.XPATH, "//[text()='ULTIMATEQA.COM’S']")
    __error_list = (By.CSS_SELECTOR, 'ul[class="form-error__list"]')
    __terms_page_agreement = (By.XPATH, "//span[text()='SERVICE AGREEMENT AND TERMS OF USE']")

    @allure.step
    def is_title_visible(self) -> 'bool':
        return self._is_displayed(self.__title)

    @allure.step
    def title_value(self):
        element = self._get_value(self.__title)
        return element

    @allure.step
    def set_first_name(self, name):
        self._send_keys(self.__first_name, name)
        return self

    @allure.step
    def set_last_name(self, last_name):
        self._send_keys(self.__last_name, last_name)
        return self

    @allure.step
    def set_email(self, email):
        self._send_keys(self.__email, email)
        return self

    @allure.step
    def set_password(self, password):
        self._send_keys(self.__password, password)
        return self

    @allure.step
    def click_terms_checkbox(self):
        self._click(self.__terms_check_box)
        return self

    @allure.step
    def click_sign_up_button(self):
        self._click(self.__sign_up_button)
        return self

    @allure.step
    def create_new_user(self, name, last_name, email, password):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        self.click_terms_checkbox().click_sign_up_button()
        return self

    @allure.step
    def open_terms_page(self):
        self._click(self.__terms_link)
        return self

    @allure.step
    def is_user_avatar_visible(self) -> 'bool':
        return self._is_displayed(self.__user_avatar)

    @allure.step
    def is_error_list_displayed(self) -> 'bool':
        return self._is_displayed(self.__error_list)

    @allure.step
    def error_list_value(self):
        error_list = self._get_value(self.__error_list)
        return error_list

    @allure.step
    def have_account(self):
        self._click(self.__have_acc_link)
        return self

    @allure.step
    def terms_value(self):
        name = self._get_value(self.__terms_page_agreement)
        return name
