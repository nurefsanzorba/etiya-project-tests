from pages.loginpage  import LoginPage
from pages.searchpage import SearchPage


class TestSearchPage():

    def test_nat_id_11_digit_enables_search(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.search_with_11_digit_nat_id("48528397898")

        assert search_page.is_search_button_enabled() is True

    def test_only_numbers_enables_search(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.enter_nat_id_only("48528397898")

        assert search_page.is_search_button_enabled() is True

    def test_fields_disabled_after_natid(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
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
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.enter_customer_id_only("50fc415a-5eab-4c7c-ad90-88aae1ae3226")

        disabled_fields = search_page.check_fields_disabled_after_customerid()
        expected_disabled = [
            search_page.NATID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.GSMNUMBER_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)


    def test_fields_disabled_after_gsmnumber(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.enter_gsm_number_only("05556667788")

        disabled_fields = search_page.check_fields_disabled_after_gsmnumber()
        expected_disabled = [
            search_page.NATID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.CUSTOMERID_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)    

    def test_first_name_enables_search(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.enter_first_name_only("Ali")

        assert search_page.is_search_button_enabled() is True

    def test_last_name_enables_search(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        search_page = SearchPage(driver, wait)
        search_page.enter_last_name_only("Veli")

        assert search_page.is_search_button_enabled() is True



    def test_nat_id_less_than_11_digit_enables_search(self,driver,wait):
       login_page = LoginPage(driver, wait)
       login_page.load_login()
       login_page.login("test","123456")


      
       search_page = SearchPage(driver, wait)
       search_page.search_with_11_digit_nat_id("163223")

       assert search_page.get_error_message() == "NAT ID must be an 11-digit number." 


    def test_gsm_number_not_between_10_and_15_digit_enables_search(self,driver,wait):
       login_page = LoginPage(driver, wait)
       login_page.load_login()
       login_page.login("test","123456")

       search_page = SearchPage(driver, wait)
       search_page.enter_gsm_number_only("1457223")

       assert search_page.get_error_message() == "GSM Number must be between 10 to 15 digits."       

         
    def test_clear_button_clears_all_fields(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test","123456")

        search_page = SearchPage(driver, wait)
    
    
        search_page.enter_nat_id_only("16322367900")
        search_page.enter_first_name_only("Ali")
        search_page.enter_last_name_only("Veli")
    
   
        search_page.click_clear_button()
    
    
        assert search_page.are_all_fields_empty() == True    
