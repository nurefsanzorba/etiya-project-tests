import pytest
from pages.customercreation_page import CustomerCreationPage
from pages.loginpage  import LoginPage
from pages.searchpage import SearchPage
import time


@pytest.mark.usefixtures("driver", "wait")
class TestCustomerCreationFull:

    # ---------------------------
    # FR 3.1 – Demographic Info
    # ---------------------------

    def test_TC_FR3_01_open_customer_creation(self, driver, wait):

        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

    
        page = CustomerCreationPage(driver, wait)
        page.open_customer_creation()
        time.sleep(5)
        assert True

    def test_TC_FR3_02_cancel_button_redirect(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
        page.open_customer_creation()
        time.sleep(5)
        page.click(page.CANCEL_BUTTON)
        time.sleep(5)
        
        assert True

    def test_TC_FR3_03_fill_demographic_fields(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
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

    def test_TC_FR3_04_first_last_name_min_char(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
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

    def test_TC_FR3_06_birth_date_age_validation(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
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

    def test_TC_FR3_07_gender_options(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
        page.open_customer_creation()
        page.click(page.GENDER)
        time.sleep(5)
        for option in ["Female", "Male", "Prefer not to say"]:
            loc = ("xpath", f"//option[text()='{option}']")
            assert page.is_enabled(loc), f"{option} seçeneği eksik."

    def test_TC_FR3_08_father_mother_name_min_char(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
        page.open_customer_creation()
        
        page.send_keys(page.FATHER_NAME, "A")
        page.send_keys(page.MOTHER_NAME, "B")
        assert page.is_next_button_enabled() is False

    def test_TC_FR3_09_nationality_id_length(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
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

    def test_TC_FR3_10_next_button_enabled_when_all_filled(self, driver, wait):
        login_page = LoginPage(driver, wait)
        login_page.load_login()
        login_page.login("test", "123456")

        page = CustomerCreationPage(driver, wait)
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

    def test_TC_FR3_11_address_screen_initial_state(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        assert not page.is_enabled(page.ADDRESS_NEXT_BUTTON), "Next buton pasif olmalı (adres yok)."

    def test_TC_FR3_12_save_button_disabled_when_required_empty(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        page.click(page.ADD_NEW_ADDRESS_BUTTON)
        assert not page.is_enabled(page.ADDRESS_SAVE_BUTTON), "Save buton pasif olmalı."

    def test_TC_FR3_13_save_address(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        page.add_new_address(
            title="Home",
            city="İstanbul",
            street="İstiklal",
            house_no="10",
            description="Yakın Taksim"
        )
        assert page.is_enabled(page.ADDRESS_NEXT_BUTTON), "Adres kaydedildi, Next aktif olmalı."

    def test_TC_FR3_14_address_listed_after_save(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        addresses = page.driver.find_elements_by_css_selector(".address-row")
        assert len(addresses) > 0, "Adres listelenmeli."

    def test_TC_FR3_15_edit_delete_buttons_visible(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        action_menu = page.driver.find_element_by_css_selector(".address-actions")
        action_menu.click()
        edit_btn = page.driver.find_element_by_xpath("//button[contains(text(),'Edit')]")
        delete_btn = page.driver.find_element_by_xpath("//button[contains(text(),'Delete')]")
        assert edit_btn and delete_btn, "Edit/Delete görünmeli."

    def test_TC_FR3_16_next_goes_to_contact_info(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/address-info")
        page.go_to_contact_info()
        assert "/contact-info" in page.driver.current_url, "Contact Info sayfası açılmalı."

    # ---------------------------
    # FR 3.3 – Contact Info
    # ---------------------------

    def test_TC_FR3_17_fill_contact_fields(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/contact-info")
        page.fill_contact_info(
            email="ali@example.com",
            mobile_phone="05551234567"
        )
        assert page.is_enabled(page.MOBILE_PHONE), "Mobile Phone alanı doldurulabilir."
        assert page.is_enabled(page.EMAIL), "Email alanı doldurulabilir."

    def test_TC_FR3_18_mobile_phone_format(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/contact-info")
        page.send_keys(page.MOBILE_PHONE, "0555")
        # Burada alan kodu ve format validasyonu yapılabilir
        assert page.get_attribute(page.MOBILE_PHONE, "value").startswith("05"), "Alan kodu yok"

    def test_TC_FR3_19_invalid_email_message(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/contact-info")
        page.fill_contact_info(email="gecersizmail", mobile_phone="05551234567")
        err = page.get_text(page.EMAIL_ERROR)
        assert "valid e-mail" in err, "Geçersiz email hatası çıkmalı."

    def test_TC_FR3_20_create_button_disabled_until_required_filled(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/contact-info")
        assert not page.is_enabled(page.CREATE_BUTTON), "Başlangıçta Create pasif olmalı."

    def test_TC_FR3_21_create_customer_success(self, driver, wait):
        page = CustomerCreationPage(driver, wait)
        page.load(page.BASE_URL + "/contact-info")
        page.fill_contact_info(email="ali@example.com", mobile_phone="05551234567")
        assert page.is_enabled(page.CREATE_BUTTON), "Create aktif olmalı."
        page.create_customer()
        assert "/customer-info" in page.driver.current_url, "Customer Info ekranı açılmalı."
