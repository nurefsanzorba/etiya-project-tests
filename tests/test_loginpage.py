from pages.loginpage import LoginPage
import pytest

class TestloginPage():

    def test_eye_icon_should_work(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Eye Icon Control"

        eye_icon_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        _, password, _, expected_state = eye_icon_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.type_password(password)
        login_page.eye_click()
        pw_type = login_page.read_password_type_attribute()

        assert pw_type == expected_state

    def test_login_button_should_be_disabled_if_username_input_area_is_empty(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Login Button Status (Username input is empty)"

    
        username_empty_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_state = username_empty_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        is_enabled = login_page.login_button_control()

        assert is_enabled == expected_state

    def test_login_button_should_be_disabled_if_password_input_area_is_empty(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Login Button Status (Password input is empty)"

        password_empty_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_state = password_empty_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        is_enabled = login_page.login_button_control()

        assert is_enabled == expected_state

    def test_login_button_should_be_disabled_if_both_input_areas_are_empty(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Login Button Status (Both input areas are empty)"

        username_and_password_empty_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_state = username_and_password_empty_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        is_enabled = login_page.login_button_control()

        assert is_enabled == expected_state

    def test_login_button_should_be_disabled_until_two_characters_entered_to_both_input_areas(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Login Button Status (Less than two character entered to the both input areas)"

        username_and_password_less_than_2_char_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_state = username_and_password_less_than_2_char_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        is_enabled = login_page.login_button_control()

        assert is_enabled == expected_state

    def test_login_button_should_be_enabled_two_or_more_characters_entered_to_both_input_areas(self, wait, driver, ui_validation_params):

        TARGET_SCENARIO = "Login Button Status (Two or more characters entered to the both input areas)"

        username_and_password_2_or_more_char_scenario = next(
            (u, p, t, s) for u, p, t, s in ui_validation_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_state = username_and_password_2_or_more_char_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        is_enabled = login_page.login_button_control()

        assert is_enabled == expected_state



    def test_invalid_password_should_give_wrong_username_or_password_error(self, wait, driver, negative_login_params):

        TARGET_SCENARIO = "Wrong Password"

        invalid_password_scenario = next(
            (u, p, t, s) for u, p, t, s in negative_login_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_error = invalid_password_scenario
        
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        err_text = login_page.get_error_text()

        assert err_text == expected_error

    def test_invalid_username_should_give_wrong_username_or_password_error(self, wait, driver, negative_login_params):

        TARGET_SCENARIO = "Wrong Username"

        invalid_username_scenario = next(
            (u, p, t, s) for u, p, t, s in negative_login_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_error = invalid_username_scenario
        
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        err_text = login_page.get_error_text()

        assert err_text == expected_error

    def test_invalid_username_and_password_should_give_wrong_username_or_password_error(self, wait, driver, negative_login_params):

        TARGET_SCENARIO = "Wrong Username and Password"

        invalid_username_and_password_scenario = next(
            (u, p, t, s) for u, p, t, s in negative_login_params if t == TARGET_SCENARIO
        )
        username, password, _, expected_error = invalid_username_and_password_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)
        err_text = login_page.get_error_text()

        assert err_text == expected_error


    def test_valid_login(self, wait, driver, positive_login_params):

        TARGET_SCENARIO = "Correct Normal User"

        valid_username_and_password_scenario = next(
            (u, p, s) for u, p, s in positive_login_params if s == TARGET_SCENARIO
        )
        username, password, _ = valid_username_and_password_scenario

        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login(username, password)

        assert True

    





