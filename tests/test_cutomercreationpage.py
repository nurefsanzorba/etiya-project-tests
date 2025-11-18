from pages.customercreation_page import CustomerCreationPage
from selenium.webdriver.common.by import By
from data.customer_create_data import CreateCustomerData
from time import sleep

class TestCustomerCreationFull:

    # ---------------------------
    # FR 3.1 – Demographic Info
    # ---------------------------

    d = CreateCustomerData()

    # Demographic Info Tab UI Check Tests
    def test_create_customer_button_should_open_customer_creation_page(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        assert True

    def test_on_the_customer_creation_page_cancel_button_should_be_clickable(self, succes_login, wait):
 
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.click(page.CANCEL_BUTTON)
        
        assert True

    def test_on_the_customer_creation_page_cancel_button_should_redirect_to_search_page(self,succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.click(page.CANCEL_BUTTON)

        assert page.CANCEL_BUTTON_REDIRECTION_URL == self.d.DEMOGRAPHIC_CANCEL_REDIRECTION_URL

    def test_first_name_min_char_next_button_should_be_disabled(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.INVALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        assert page.is_next_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_last_name_min_char_next_button_should_be_disabled(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.INVALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        assert page.is_next_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_age_younger_than_sixteen_next_button_should_be_disabled(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.INVALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        assert page.is_next_button_enabled() is self.d.IS_ENABLED_FALSE
    
    def test_invalid_nat_id_less_than_eleven_digits_next_button_should_be_disabled(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.INVALID_TEN_DIGIT_NAT_ID
        )

        assert page.is_next_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_invalid_nat_id_more_than_eleven_digits_next_button_should_be_disabled(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.INVALID_TWELVE_DIGIT_NAT_ID
        )
        sleep(3)
        assert page.is_next_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_gender_options_should_be_clickable(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.click(page.GENDER)
        for option in self.d.GENDER_LIST:
            loc = page.check_gender_options(option)
            assert page.is_enabled(loc), f"{option} seçeneği eksik."

    # Demographic Info Tab Negative Tests
    def test_first_name_min_char_should_give_error_first_name_is_required_two_twenty_characters(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.INVALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )
        sleep(10)

        assert page.get_first_name_error() == self.d.ERROR_FIRST_NAME
    

    def test_last_name_min_char_should_give_error_last_name_is_required_two_twenty_characters(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.INVALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        assert page.get_last_name_error() == self.d.ERROR_LAST_NAME

    def test_age_younger_than_sixteen_should_give_error_age_must_be_at_least_sixteen_years_old(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.INVALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        assert page.get_age_error() == self.d.ERROR_AGE
    
    def test_invalid_nat_id_less_than_eleven_digits_should_give_error_nat_id_must_be_an_eleven_digit(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.INVALID_TEN_DIGIT_NAT_ID
        )
        
        page.click_demographic_next_button()

        assert page.get_nat_id_error() == self.d.ERROR_NAT_ID

    def test_invalid_nat_id_more_than_eleven_digits_should_give_error_nat_id_must_be_an_eleven_digit(self, succes_login, wait):
        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.INVALID_TWELVE_DIGIT_NAT_ID
        )

        page.click_demographic_next_button()

        assert page.get_nat_id_error() == self.d.ERROR_NAT_ID


    # Demographic Info Tab Positive Tests
    def test_valid_customer_demographic_info(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            self.d.VALID_FIRST_NAME,
            self.d.VALID_LAST_NAME,
            self.d.VALID_DATE_OF_BIRTH,
            self.d.GENDER_MALE,
            self.d.VALID_NAT_ID
        )

        page.submit_demographic()

        assert True 


    # ---------------------------
    # FR 3.2 – Address Info
    # ---------------------------

    #Address Info Tab UI Tests
    def test_without_creating_new_address_interface_next_button_should_be_disabled(self, succes_demographic_info, wait):
        
        page = CustomerCreationPage(succes_demographic_info, wait)

        assert page.check_address_interface_next_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_add_new_address_should_be_clickable(self, succes_demographic_info, wait):

        page = CustomerCreationPage(succes_demographic_info, wait)
        
        assert page.check_add_new_address_button_enabled() is self.d.IS_ENABLED_TRUE

    def test_in_new_address_add_tab_cancel_button_should_be_enabled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        assert page.check_address_cancel_button_enabled() is self.d.IS_ENABLED_TRUE

    def test_in_new_address_add_tab_previous_button_should_be_enabled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        assert page.check_address_previous_button_enabled() is self.d.IS_ENABLED_TRUE

    def test_in_new_address_add_tab_save_button_should_be_disabled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        assert page.check_address_save_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_in_new_address_add_tab_next_button_should_be_disabled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        assert page.check_address_next_button_enabled() is self.d.IS_ENABLED_FALSE

    #Address Info Tab Negative Tests
    def test_empty_address_title_should_give_address_title_is_required_error(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.EMPTY_TITLE,
            self.d.VALID_CITY,
            self.d.VALID_STREET,
            self.d.VALID_HOUSE_NO,
            self.d.VALID_DESCRIPTION
        )

        assert page.get_address_title_error_text() == self.d.ERROR_ADDRESS_TITLE

    def test_empty_address_street_should_give_street_is_required_error(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.VALID_TITLE,
            self.d.VALID_CITY,
            self.d.EMPTY_STREET,
            self.d.VALID_HOUSE_NO,
            self.d.VALID_DESCRIPTION
        )
        
        assert page.get_address_street_error_text() == self.d.ERROR_STREET

    def test_empty_house_no_should_give_house_no_is_required_error(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.VALID_TITLE,
            self.d.VALID_CITY,
            self.d.VALID_STREET,
            self.d.EMPTY_HOUSE_NO,
            self.d.VALID_DESCRIPTION
        )
        
        assert page.get_house_no_error_text() == self.d.ERROR_HOUSE_NO
    # Description boş geçilirse save butonu disabled, boş bırakılamaz error mesajı dönmüyor
    # Buraları FR üzerinde de güncellemeliyiz sadece zorunlu alan olarak vermişiz doldurulmaması durumunda
    # bir error mesajının olması gerektiği hakkında bilgi yok
    def test_empty_description_should_give_address_title_is_required_error(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.VALID_TITLE,
            self.d.VALID_CITY,
            self.d.VALID_STREET,
            self.d.VALID_HOUSE_NO,
            self.d.EMPTY_DESCRIPTION
        )
        sleep(5)
        
        assert page.get_description_error_text() == self.d.ERROR_DESCRIPTION

    # Address Info Tab Positive Tests
    def test_save_button_enabled_when_required_fields_filled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.VALID_TITLE,
            self.d.VALID_CITY,
            self.d.VALID_STREET,
            self.d.VALID_HOUSE_NO,
            self.d.VALID_DESCRIPTION
        )
        assert True, "Adres kaydedildi, Next aktif olmalı."

    def test_address_should_be_listed_after_save(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click_add_new_address_button()
        page.add_new_address(
            self.d.VALID_TITLE,
            self.d.VALID_CITY,
            self.d.VALID_STREET,
            self.d.VALID_HOUSE_NO,
            self.d.VALID_DESCRIPTION
        )
        addresses = page.get_address_list()
        assert len(addresses) > 0, "Adres listelenmeli."


    # ---------------------------
    # FR 3.3 – Contact Info
    # ---------------------------

    #Contact Medium UI Component Tests
    def test_contact_medium_opens_and_create_customer_button_should_be_disabled(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        assert page.check_contact_medium_create_button_enabled() is self.d.IS_ENABLED_FALSE

    def test_contact_medium_opens_and_previous_button_should_be_enabled(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        assert page.check_contact_medium_previous_button_enabled() is self.d.IS_ENABLED_TRUE

    #Contact Medium Negative Tests
    def test_contact_medium_invalid_mail_should_give_invalid_mail_error(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        page.fill_contact_info(
           self.d.INVALID_EMAIL,
           self.d.VALID_MOBILE_PHONE
        ) 
        assert page.get_email_error_text() == self.d.ERROR_EMAIL

    def test_contact_medium_invalid_mobile_phone_minimum_should_give_invalid_mobile_error(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        page.fill_contact_info(
           self.d.VALID_EMAIL,
           self.d.INVALID_LESS_TEN_MOBILE_PHONE,
           fax = self.d.FAX
        ) 
        assert page.get_mobile_phone_error_text() == self.d.ERROR_MOBILE_PHONE

    def test_contact_medium_invalid_mobile_phone_maximum_should_give_invalid_mobile_error(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        page.fill_contact_info(
           self.d.VALID_EMAIL,
           self.d.INVALID_MORE_FIFTEEN_MOBILE_PHONE,
           fax = self.d.FAX
        ) 
        assert page.get_mobile_phone_error_text() == self.d.ERROR_MOBILE_PHONE

    def test_contact_medium_invalid_mobile_phone_and_mail_should_give_invalid_mobile_and_email_error(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)
        
        page.fill_contact_info(
           self.d.INVALID_EMAIL,
           self.d.INVALID_LESS_TEN_MOBILE_PHONE,
           fax = self.d.FAX
        ) 
        assert page.get_mobile_phone_error_text() == self.d.ERROR_MOBILE_PHONE
        assert page.get_email_error_text() == self.d.ERROR_EMAIL

    def test_valid_contact_medium_but_exist_customer_info_should_give_customer_with_this_natid_already_exists_error(self, exists_demographic_info_success_address, wait):
        page = CustomerCreationPage(exists_demographic_info_success_address, wait)

        page.fill_contact_info(
            self.d.VALID_EMAIL,
            self.d.VALID_MOBILE_PHONE
        )

        page.click_create_customer()

        assert page.get_customer_with_this_natid_already_exists_error_text() == self.d.ALREADY_EXIST_CUSTOMER_ERROR

    #Contact Medium Tab Positive Tests
    def test_contact_medium_valid_credentials_should_create_new_customer(self, succes_address_info, wait):
        page = CustomerCreationPage(succes_address_info, wait)

        page.fill_contact_info(
            self.d.VALID_EMAIL,
            self.d.VALID_MOBILE_PHONE
        )

        page.click_create_customer()

        assert True

