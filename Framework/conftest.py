import json
from contextlib import suppress

import allure
import pytest

from Framework.CONSTANTS import ROOT_DIR
from Framework.data_classes.user import User
from Framework.page_objects.all_courses_page.all_courses_page import AllCourses
from Framework.page_objects.course_page.course_page import CoursePage
from Framework.page_objects.forgot_password_page.forgot_password_page import ForgotPass
from Framework.page_objects.forgot_password_page.reset_page import ResetPage
from Framework.page_objects.login_window.login_window import LoginWindow
from Framework.page_objects.register_page.register_page import RegisterPage
from Framework.utilities.configuration import Configuration
from Framework.utilities.driver_factory import DriverFactory


def pytest_configure(config):
    """
    This function register an additional marker
    :param config:
    """
    config.addinivalue_line(
        "markers", 'regression: for regression'
    )
    config.addinivalue_line(
        "markers", 'smoke: for smoke'
    )


@pytest.fixture()
def env():
    """
    This fixture gives access to configuraton.json
    :return: dict
    """
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    configs = Configuration(**json_to_dict)
    return configs


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_driver(env, request):
    """fixture for creating driver"""
    driver = DriverFactory.create_driver(env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def open_login_window(create_driver):
    """fixture for open Login Window"""
    return LoginWindow(create_driver)


@pytest.fixture()
def open_register_window(create_driver, open_login_window):
    """fixture for open user Registration"""
    login = open_login_window.click_on_sing_in()
    driver = create_driver.execute_script("window.scrollTo(100, 550)")
    register = login.click_create_new_acc()
    return RegisterPage(create_driver)


@pytest.fixture()
def open_forgot_pass_window(create_driver, open_login_window):
    """fixture for open user reset password"""
    login_window = open_login_window.click_on_sing_in().click_on_forgot_link()
    return ForgotPass(create_driver)


@pytest.fixture()
def reset_page(create_driver):
    """fixture for open user reset password"""
    return ResetPage(create_driver)


@pytest.fixture()
def main_screen(create_driver):
    """fixture for all courses screen"""
    return AllCourses(create_driver)


@pytest.fixture()
def scroll_main_screen(create_driver, open_login_window):
    """fixture for open user Registration"""
    driver = create_driver.execute_script("window.scrollTo(0, 1300)")
    return AllCourses(create_driver)


@pytest.fixture()
def open_course_page(create_driver, main_screen):
    """fixture for open Course Info"""
    course = main_screen.choose_course()
    return CoursePage(create_driver)


@pytest.fixture()
def scroll_course_page(create_driver, main_screen):
    """fixture for open Course Info and scroll the page"""
    course = main_screen.choose_course()
    driver = create_driver.execute_script("window.scrollTo(0, 520)")
    return CoursePage(create_driver)


@pytest.fixture()
def scroll_course_page_to_middle(create_driver, main_screen):
    """fixture for open Course Info and scroll the page"""
    course = main_screen.choose_course()
    driver = create_driver.execute_script("window.scrollTo(0, 1600)")
    return CoursePage(create_driver)


@pytest.fixture()
def scroll_course_page_to_end(create_driver, main_screen):
    """fixture for open Course Info and scroll the page"""
    course = main_screen.choose_course()
    driver = create_driver.execute_script("window.scrollTo(0, 1900)")
    return CoursePage(create_driver)


@pytest.fixture()
def create_user():
    return User()
