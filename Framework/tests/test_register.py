import pytest


@pytest.mark.smoke
def test_open_register_user_window(open_register_window):
    register = open_register_window
    assert register.is_title_visible() is True, "Open Login window to provide registration"

@pytest.mark.skip('Skipped test')
@pytest.mark.smoke
def test_register_user(open_register_window):  # possible captcha
    register_window = open_register_window
    registration = register_window.create_new_user('Valerchik', 'Nevalechick', 'Valerchik_50@gmail.com', 'sonechko50')
    assert registration.user_avatar_is_visible() is True


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
def test_redirect_to_terms_page(open_register_window):
    register_window = open_register_window
    terms = register_window.open_terms_page()
    assert terms.is_title_visible() is True
    assert terms.terms_value() == 'SERVICE AGREEMENT AND TERMS OF USE'


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
@pytest.mark.parametrize("name, last_name", [('', 'last'), ('first', '')])
def test_register_user_with_empty_name_or_lastname(open_register_window, name, last_name):  # possible captcha
    register_window = open_register_window
    registration = register_window.create_new_user(name, last_name, 'Valerchik_50@gmail.com', 'sonechko50')
    assert registration.error_list() is True
    assert registration.error_list_value() == "First name can't be blank"  # for name parametrize
    assert registration.error_list_value() == "Last name can't be blank"  # for last_name parametrize


@pytest.mark.skip('Skipped test')
@pytest.mark.regression
@pytest.mark.parametrize("email, password", [('', 'last@gmail.com'), ('first500', '')])
def test_register_user_with_empty_email_or_password(open_register_window, email, password):  # possible captcha
    register_window = open_register_window
    registration = register_window.create_new_user('Valerchik', 'nevalerchik', email, password)
    assert registration.error_list() is True
    assert registration.error_list_value() == "Email can't be blank"  # for Email parametrize
    assert registration.error_list_value() == "Password can't be blank"  # for Password parametrize

@pytest.mark.skip('Skipped test')
@pytest.mark.smoke
def test_registration_with_empty_fields(open_register_window):
    register_window = open_register_window
    registration = register_window.click_sign_up_button()
    assert registration.error_list_value() == "Email can't be blank" "Password can't be blank" "First name can't be blank" "Last name can't be blank"


@pytest.mark.skip('Skipped test')
@pytest.mark.smoke
def test_return_to_login(open_register_window, open_login_window):
    register_window = open_register_window
    registration = register_window.have_account()
    login_page = open_login_window
    assert login_page.is_sign_in_button_displayed() is True
