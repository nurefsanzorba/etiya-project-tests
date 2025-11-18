from pages.loginpage import LoginPage
from data.login_data import LoginConstants
class TestloginPage():
    c = LoginConstants()

    #UI TESTS
    def test_eye_icon_should_work(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_password(self.c.VALID_PASSWORD)
        login_page.eye_click()
        pw_type = login_page.read_password_type_attribute()

        assert pw_type == self.c.PASSWORD_INPUT_ATTRIBUTE

    def test_login_button_should_be_disabled_if_username_input_area_is_empty(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_username(self.c.EMPTY_USERNAME)
        login_page.type_password(self.c.VALID_PASSWORD)
        is_enabled = login_page.login_button_control()

        assert is_enabled == self.c.IS_ENABLED_FALSE

    def test_login_button_should_be_disabled_if_password_input_area_is_empty(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_username(self.c.VALID_USERNAME)
        login_page.type_password(self.c.EMPTY_PASSWORD)
        is_enabled = login_page.login_button_control()

        assert is_enabled == self.c.IS_ENABLED_FALSE

    def test_login_button_should_be_disabled_if_both_input_areas_are_empty(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_username(self.c.EMPTY_USERNAME)
        login_page.type_password(self.c.EMPTY_PASSWORD)
        is_enabled = login_page.login_button_control()

        assert is_enabled == self.c.IS_ENABLED_FALSE

    def test_login_button_should_be_disabled_until_two_characters_entered_to_both_input_areas(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_username(self.c.ONE_USERNAME)
        login_page.type_password(self.c.ONE_PASSWORD)
        is_enabled = login_page.login_button_control()

        assert is_enabled == self.c.IS_ENABLED_FALSE

    def test_login_button_should_be_enabled_two_or_more_characters_entered_to_both_input_areas(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.type_username(self.c.VALID_USERNAME)
        login_page.type_password(self.c.VALID_PASSWORD)
        is_enabled = login_page.login_button_control()

        assert is_enabled == self.c.IS_ENABLED_TRUE

    #Negative Tests
    def test_invalid_password_should_give_wrong_username_or_password_error(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login(self.c.VALID_USERNAME, self.c.INVALID_PASSWORD)
        err_text = login_page.get_error_text()

        assert err_text == self.c.ERROR_MESSAGE_WRONG_CREDENTIALS

    def test_invalid_username_should_give_wrong_username_or_password_error(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login(self.c.INVALID_USERNAME, self.c.VALID_PASSWORD)
        err_text = login_page.get_error_text()

        assert err_text == self.c.ERROR_MESSAGE_WRONG_CREDENTIALS

    def test_invalid_username_and_password_should_give_wrong_username_or_password_error(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login(self.c.INVALID_USERNAME, self.c.INVALID_PASSWORD)
        err_text = login_page.get_error_text()

        assert err_text == self.c.ERROR_MESSAGE_WRONG_CREDENTIALS


    def test_valid_login(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login(self.c.VALID_USERNAME, self.c.VALID_PASSWORD)

        assert True

    





