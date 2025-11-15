from pages.searchpage import SearchPage
from data.search_data import SearchData

class TestSearchPage():

    c = SearchData()

    def test_nat_id_11_digit_enables_search(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.search_with_11_digit_nat_id(self.c.VALID_NATID)

        assert search_page.is_search_button_enabled() is True

    def test_only_numbers_enables_search(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_nat_id_only(self.c.VALID_NATID)

        assert search_page.is_search_button_enabled() is True

    def test_fields_disabled_after_natid(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_nat_id_only(self.c.VALID_NATID)

        disabled_fields = search_page.check_fields_disabled_after_natid()
        expected_disabled = [
            search_page.CUSTOMERID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.GSMNUMBER_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)

    def test_fields_disabled_after_customerid(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_customer_id_only(self.c.CUSTOMER_NUMBER)

        disabled_fields = search_page.check_fields_disabled_after_customerid()
        expected_disabled = [
            search_page.NATID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.GSMNUMBER_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)


    def test_fields_disabled_after_gsmnumber(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_gsm_number_only(self.c.VALID_GSM)

        disabled_fields = search_page.check_fields_disabled_after_gsmnumber()
        expected_disabled = [
            search_page.NATID_INPUT,
            search_page.ACCOUNTNUMBER_INPUT,
            search_page.CUSTOMERID_INPUT,
            search_page.ORDERNUMBER_INPUT
        ]
        assert set(disabled_fields) == set(expected_disabled)    

    def test_first_name_enables_search(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_first_name_only(self.c.FIRST_NAME)

        assert search_page.is_search_button_enabled() is True

    def test_last_name_enables_search(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
        search_page.enter_last_name_only(self.c.LAST_NAME)

        assert search_page.is_search_button_enabled() is True



    def test_nat_id_less_than_11_digit_enables_search(self,succes_login,wait):

       search_page = SearchPage(succes_login, wait)
       search_page.search_with_11_digit_nat_id(self.c.INVALID_NATID)

       assert search_page.get_error_message() == self.c.ERROR_INVALID_NATID


    def test_gsm_number_not_between_10_and_15_digit_enables_search(self,succes_login,wait):

       search_page = SearchPage(succes_login, wait)
       search_page.enter_gsm_number_only(self.c.INVALID_GSM)

       assert search_page.get_error_message() == self.c.ERROR_INVALID_GSM      

         
    def test_clear_button_clears_all_fields(self, succes_login, wait):

        search_page = SearchPage(succes_login, wait)
    
    
        search_page.enter_nat_id_only(self.c.VALID_NATID)
        search_page.enter_first_name_only(self.c.FIRST_NAME)
        search_page.enter_last_name_only(self.c.LAST_NAME)
    
   
        search_page.click_clear_button()
    
    
        assert search_page.are_all_fields_empty() == True    
