import pytest


@pytest.mark.smoke
def test_user_search(open_login_window, env):  # possible captcha
    login = open_login_window.login(env.email, env.password)
    screen = login.enter_something_in_search('Das')
    screen = login.press_enter()
    assert screen.is_search_title_visible() is True


@pytest.mark.smoke
@pytest.mark.skip('Skipped test')
def test_select_course(main_screen):  # can be tested
    screen = main_screen.choose_course()
    assert screen.is_title_visible() is True


@pytest.mark.regression
@pytest.mark.skip('Skipped test')
def test_click_on_second_page(scroll_main_screen):
    screen = scroll_main_screen.open_collections()
    screen = scroll_main_screen.choose_page()
    assert screen.is_first_course_invisible() is False


@pytest.mark.regression
@pytest.mark.skip('Skipped test')
def test_change_page(scroll_main_screen):
    screen = scroll_main_screen.open_collections()
    screen = scroll_main_screen.next_page()
    assert screen.is_first_course_invisible() is False


@pytest.mark.regression
@pytest.mark.skip('Skipped test')
def test_open_more_courses(scroll_main_screen):
    main_screen = scroll_main_screen.open_more_courses()
    assert main_screen.is_main_title_displayed() is False
