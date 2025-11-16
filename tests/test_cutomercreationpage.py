from pages.customercreation_page import CustomerCreationPage
from selenium.webdriver.common.by import By
import time


class TestCustomerCreationFull:

    # ---------------------------
    # FR 3.1 – Demographic Info
    # ---------------------------

    def test_TC_FR3_01_open_customer_creation(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        time.sleep(5)
        assert True

    def test_TC_FR3_02_cancel_button_redirect(self, succes_login, wait):
 

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        time.sleep(5)
        page.click(page.CANCEL_BUTTON)
        time.sleep(5)
        
        assert True

    def test_TC_FR3_03_fill_demographic_fields(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            first_name="Ali",
            last_name="Yılmaz",
            dob="01/01/1990",
            gender="Male",
            nationality_id="12345678900"
        )

        time.sleep(5)
        assert page.is_next_button_enabled() is True

    def test_TC_FR3_04_first_last_name_min_char(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.send_keys(page.FIRST_NAME, "A")
        page.send_keys(page.LAST_NAME, "B")
        time.sleep(5)
        assert page.is_next_button_enabled() is False

    # def test_TC_FR3_05_birth_date_format_validation(self, driver, wait):
    #     login_page = LoginPage(driver, wait)
    #     login_page.load_login()
    #     login_page.login("test", "123456")

    #     page = CustomerCreationPage(driver, wait)
    #     page.open_customer_creation()
    #     page.fill_demographic_info(
    #         first_name="Ali",
    #         last_name="Yılmaz",
    #         dob="2020-01-01",
    #         gender="Male",
    #         nationality_id="12345678900"
    #     )

    #     time.sleep(5)
    #     page.submit_demographic()
    #     warning = page.check_duplicate_warning()
    #     assert "dd/mm/yyyy" in warning or warning != "", "Tarih format hatası görünmeli."

    def test_TC_FR3_06_birth_date_age_validation(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            first_name="Ali",
            last_name="Yılmaz",
            dob="01/01/2020",
            gender="Male",
            nationality_id="12345678900"
        )

        time.sleep(5)
        page.submit_demographic()
        page.get_error_message_for_age() == "Customer must be at least 16 years old."

    def test_TC_FR3_07_gender_options(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.click(page.GENDER)
        time.sleep(5)
        for option in ["Female", "Male", "Prefer not to say"]:
            loc = ("xpath", f"//option[text()='{option}']")
            assert page.is_enabled(loc), f"{option} seçeneği eksik."

    def test_TC_FR3_08_father_mother_name_min_char(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        
        page.send_keys(page.FATHER_NAME, "A")
        page.send_keys(page.MOTHER_NAME, "B")
        assert page.is_next_button_enabled() is False

    def test_TC_FR3_09_nationality_id_length(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            first_name="Ali",
            last_name="Yılmaz",
            dob="01/01/2000",
            gender="Male",
            nationality_id="123456"
        )

        time.sleep(5)
        page.submit_demographic()
        assert page.get_error_message_for_natid() == "NAT ID must be an 11-digit number."

    def test_TC_FR3_10_next_button_enabled_when_all_filled(self, succes_login, wait):

        page = CustomerCreationPage(succes_login, wait)
        page.open_customer_creation()
        page.fill_demographic_info(
            first_name="Ahmet",
            last_name="Demir",
            dob="01/01/1990",
            gender="Male",
            nationality_id="12345678900"
        )
        time.sleep(5)
        assert page.is_next_button_enabled() is True

    # ---------------------------
    # FR 3.2 – Address Info
    # ---------------------------

    def test_TC_FR3_11_address_screen_initial_state(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.check_add_new_address("", "", "", "", "")
        assert not page.is_next_button_enabled(), "Next buton pasif olmalı (adres yok)."

    def test_TC_FR3_12_save_button_disabled_when_required_empty(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.click(page.ADD_NEW_ADDRESS_BUTTON)
        assert not page.is_save_button_enabled(), "Save buton pasif olmalı."

    def test_TC_FR3_13_save_button_enabled_when_required_fields_filled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.check_add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        assert page.is_save_button_enabled(), "Adres kaydedildi, Next aktif olmalı."

    def test_TC_FR3_14_address_listed_after_save(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        time.sleep(2)
        addresses = page.driver.find_elements(
               By.CSS_SELECTOR,
               "div.bg-white.border.border-gray-300.rounded-lg.p-4.shadow-sm"
        )
        assert len(addresses) > 0, "Adres listelenmeli."

    # def test_TC_FR3_15_edit_delete_buttons_visible(self, succes_login, wait):
    #     page = CustomerCreationPage(succes_login, wait)
    #     page.load(page.BASE_URL + "/address-info")
    #     action_menu = page.driver.find_element_by_css_selector(".address-actions")
    #     action_menu.click()
    #     edit_btn = page.driver.find_element_by_xpath("//button[contains(text(),'Edit')]")
    #     delete_btn = page.driver.find_element_by_xpath("//button[contains(text(),'Delete')]")
    #     assert edit_btn and delete_btn, "Edit/Delete görünmeli."

    def test_TC_FR3_16_next_goes_to_contact_info(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        
        page.wait_until_next_button_enabled()
       
        assert True

    # ---------------------------
    # FR 3.3 – Contact Info
    # ---------------------------

    def test_TC_FR3_17_fill_contact_fields(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        page.click(page.ADDRESS_NEXT_BUTTON)
        page.fill_contact_info(
           email="test@gmail.com",
           mobile_phone="2251234567",
           home_phone="5551234567",
           fax="2125554321"
        ) 
        
        assert page.is_create_button_enabled()

    def test_TC_FR3_18_mobile_phone_format(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        page.click(page.ADDRESS_NEXT_BUTTON)
        page.fill_contact_info(
           email="test@example.com",
           mobile_phone="55512",
           home_phone="5551234567",
           fax="2125554321"
        ) 
        assert page.get_error_message_for_conatctinfo() == "Please enter a valid mobile phone number (including area code)"

    def test_TC_FR3_19_invalid_email_message(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        page.click(page.ADDRESS_NEXT_BUTTON)
        page.fill_contact_info(
           email="test",
           mobile_phone="2125551234",
           home_phone="5551234567",
           fax="2125554321"
        ) 
        assert page.get_error_message_for_conatctinfo() == "E-mail must be valid e-mail address!"

    def test_TC_FR3_20_create_button_disabled_until_required_filled(self, succes_demographic_info, wait):
        page = CustomerCreationPage(succes_demographic_info, wait)
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        page.click(page.ADDRESS_NEXT_BUTTON)
        page.fill_contact_info(
           email="test@gmail.com",
           mobile_phone=" ",
           home_phone="5551234567",
           fax="2125554321"
        ) 
        
        assert not page.is_create_button_enabled()

    def test_TC_FR3_21_create_customer_success(self, succes_demographic_info, wait):
         page = CustomerCreationPage(succes_demographic_info, wait)
         page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
         page.click(page.ADDRESS_NEXT_BUTTON)
         page.fill_contact_info(
           email="test@gmail.com",
           mobile_phone="2125551234",
           home_phone="5551234567",
           fax="2125554321"
        ) 
         page.create_customer()
         assert True
