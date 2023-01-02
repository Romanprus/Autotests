import pytest


@pytest.mark.smoke
def test_click_on_forgot_pass(open_forgot_pass_window):
    forgot_window = open_forgot_pass_window
    value = forgot_window.title_value()
    assert forgot_window.title_value() == "Forgot your Password?"


@pytest.mark.smoke
def test_reset_password(open_forgot_pass_window, reset_page, env):
    reset = open_forgot_pass_window
    reset = open_forgot_pass_window.reset_password(env.reset_email)
    assert reset.is_sucssess_title_displayed() is True and reset.title_value() == "Help is on the way!"


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
def test_reset_without_email(open_forgot_pass_window):
    reset = open_forgot_pass_window.reset_pass_with_empty_mail()
    assert reset.is_email_field_present() is True


@pytest.mark.skip('Skipped test')
@pytest.mark.smoke
def test_return_to_login_after_password_reset(open_forgot_pass_window, env):
    reset = open_forgot_pass_window
    reset = open_forgot_pass_window.reset_password(env.reset_email).back_to_sign_in_screen()
    assert reset.is_sign_in_button_displayed() is True


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
def test_return_to_login_page(open_forgot_pass_window):
    reset = open_forgot_pass_window
    reset = open_forgot_pass_window.back_to_sign_in_screen()
    assert reset.is_sign_in_button_displayed() is True
