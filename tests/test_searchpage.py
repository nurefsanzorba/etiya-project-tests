from pages.loginpage  import LoginPage
from pages.searchpage import SearchPage


class TestSearchPage():

    def test_nat_id_11_digit_enables_search(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("mutlum123456", "123456")

        search_page = SearchPage(wait, driver)
        search_page.search_with_11_digit_nat_id("48528397898")

        assert search_page.is_search_button_enabled() is True

    def test_only_numbers_enables_search(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("mutlum123456", "123456")

        search_page = SearchPage(wait, driver)
        search_page.enter_nat_id_only("48528397898")

        assert search_page.is_search_button_enabled() is True

    def test_fields_disabled_after_natid(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("deneme", "pass")

        search_page = SearchPage(wait, driver)
        search_page.enter_nat_id_only("16322367900")

        disabled_fields = search_page.check_fields_disabled_after_natid()
        expected_disabled = [
            search_page.CUSTOMERID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.GSMNUMBER_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)

    def test_fields_disabled_after_customerid(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("deneme", "pass")

        search_page = SearchPage(wait, driver)
        search_page.enter_customer_id_only("50fc415a-5eab-4c7c-ad90-88aae1ae3226")

        disabled_fields = search_page.check_fields_disabled_after_customerid()
        expected_disabled = [
            search_page.NATID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.GSMNUMBER_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)

    def test_first_name_enables_search(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("deneme", "pass")

        search_page = SearchPage(wait, driver)
        search_page.enter_first_name_only("Ali")

        assert search_page.is_search_button_enabled() is True

    def test_last_name_enables_search(self, driver, wait):
        login_page = LoginPage(wait, driver)
        login_page.load_login()
        login_page.login("deneme", "pass")

        search_page = SearchPage(wait, driver)
        search_page.enter_last_name_only("Veli")

        assert search_page.is_search_button_enabled() is True
