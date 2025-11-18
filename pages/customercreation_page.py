from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CustomerCreationPage(BasePage):

    #Redirection Url
    CANCEL_BUTTON_REDIRECTION_URL = "http://localhost:4200/b2c"

    # === Locators ===
    CREATE_CUSTOMER_BUTTON = (By.XPATH, "/html/body/app-root/app-b2c/div/div/app-search/div/div[2]/div[2]/div[2]/div[2]/button")
    CANCEL_BUTTON = (By.XPATH, "/html/body/app-root/app-b2c/div/div/app-create-customer/div/div/form/div/div[2]/button[1]")

    # Demographic info fields
    FIRST_NAME = (By.CSS_SELECTOR, "input[formcontrolname='firstName']")
    MIDDLE_NAME = (By.CSS_SELECTOR, "input[formcontrolname='middleName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[formcontrolname='lastName']")
    DOB = (By.CSS_SELECTOR, "input[formcontrolname='birthDate']")
    GENDER = (By.CSS_SELECTOR, "select[formcontrolname='gender']")
    FATHER_NAME = (By.CSS_SELECTOR, "input[formcontrolname='fatherName']")
    MOTHER_NAME = (By.CSS_SELECTOR, "input[formcontrolname='motherName']")
    NATIONALITY_ID = (By.CSS_SELECTOR, "input[formcontrolname='nationalityId']")
    DEMOGRAPHIC_NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Next']")
    ERROR_FIRST_NAME = (By.XPATH, "//p[normalize-space(text())='First Name is required (2-20 characters)']")
    ERROR_LAST_NAME = (By.XPATH, "//p[normalize-space(text())='Last Name is required (2-20 characters)']")
    ERROR_NAT_ID = (By.XPATH, "//p[normalize-space(text())='NAT ID must be an 11-digit number.']")
    ERROR_AGE = (By.XPATH, "//div[normalize-space(text())='Customer must be at least 16 years old.']")

    # Address Info
    ADD_NEW_ADDRESS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Add New Address']")
    ADDRESS_INTERFACE_NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Next']")
    ADDRESS_CANCEL_BUTTON = (By.XPATH, "//button[normalize-space(text())='Cancel']")
    ADDRESS_PREVIOUS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Previous]")
    ADDRESS_TITLE = (By.ID, "addressTitle")
    CITY = (By.CSS_SELECTOR, "select[formcontrolname='cityId']")
    STREET = (By.ID, "street")
    HOUSE_NUMBER = (By.CSS_SELECTOR, "input[formcontrolname='houseNumber']")
    ADDRESS_DESCRIPTION = (By.CSS_SELECTOR, "textarea[formcontrolname='description']")
    ADDRESS_SAVE_BUTTON = (By.XPATH, "//button[normalize-space(text())='Save']")
    ADDRESS_NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Next']")
    ADDRESS_LIST_CONTROL =(By.CSS_SELECTOR,"div.bg-white.border.border-gray-300.rounded-lg.p-4.shadow-sm")
    ERROR_ADDRESS_TITLE = (By.XPATH, "//p[normalize-space(text())='Address Title is required.']")
    ERROR_STREET = (By.XPATH, "//p[normalize-space(text())='Street is required.']")
    ERROR_HOUSE_NO = (By.XPATH, "//p[normalize-space(text())='House/Flat Number is required.']")
    ERROR_DESCRIPTION = (By.XPATH, "//p[normalize-space(text())='Address Description is required.']")

    # Contact Info
    EMAIL = (By.CSS_SELECTOR, "input[formcontrolname='email']")
    HOME_PHONE = (By.CSS_SELECTOR, "input[formcontrolname='homePhone']")
    MOBILE_PHONE = (By.CSS_SELECTOR, "input[formcontrolname='mobilePhone']")
    FAX = (By.CSS_SELECTOR, "input[formcontrolname='fax']")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space(text())='Create Customer']")
    CONTACT_MEDIUM_PREVIOUS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Previous']")
    ERROR_MOBILE_PHONE = (By.XPATH, "//p[normalize-space(text())='Please enter a valid mobile phone number (including area code)']")
    ERROR_EMAIL = (By.XPATH, "//p[normalize-space(text())='E-mail must be valid e-mail address!']")

    #MAIN ERROR CUSTOMER WITH THIS NAT ID EXISTS
    ERROR_ALREADY_EXISTS = (By.XPATH, "//p[normalize-space(text())='Customer with this national identity exists.']")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    # === Methods ===
    def open_customer_creation(self):
        self.click(self.CREATE_CUSTOMER_BUTTON)

    def fill_demographic_info(self, first_name, last_name, dob, gender, nationality_id, **kwargs):
        self.send_keys(self.FIRST_NAME, first_name)
        if kwargs.get("middle_name"):
            self.send_keys(self.MIDDLE_NAME, kwargs["middle_name"])
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.DOB, dob)
        self.click(self.GENDER)
        gender_option = (By.XPATH, f"//option[text()='{gender}']")
        self.click(gender_option)
        if kwargs.get("father_name"):
            self.send_keys(self.FATHER_NAME, kwargs["father_name"])
        if kwargs.get("mother_name"):
            self.send_keys(self.MOTHER_NAME, kwargs["mother_name"])
        self.send_keys(self.NATIONALITY_ID, nationality_id)

    def get_first_name_error(self):
        return self.get_error_text(self.ERROR_FIRST_NAME)
    
    def get_last_name_error(self):
        return self.get_error_text(self.ERROR_LAST_NAME)
    
    def get_nat_id_error(self):
        return self.get_error_text(self.ERROR_NAT_ID)
    
    def get_age_error(self):
        return self.get_error_text(self.ERROR_AGE)
    
    def click_demographic_next_button(self):
        self.click(self.DEMOGRAPHIC_NEXT_BUTTON)
    
    def check_gender_options(self, option):
        return ("xpath", f"//option[text()='{option}']")
    
    def is_next_button_enabled(self):
        return self.is_enabled(self.DEMOGRAPHIC_NEXT_BUTTON)

    def wait_until_next_button_enabled(self):
        self.wait.until(lambda d: d.find_element(*self.ADDRESS_NEXT_BUTTON).is_enabled())

    def submit_demographic(self):
            self.click(self.DEMOGRAPHIC_NEXT_BUTTON)
    
    #Address tab methods
    def check_address_interface_next_button_enabled(self):
        return self.is_enabled(self.ADDRESS_INTERFACE_NEXT_BUTTON)
    
    def check_add_new_address_button_enabled(self):
        return self.is_enabled(self.ADD_NEW_ADDRESS_BUTTON)
    
    def click_add_new_address_button(self):
        return self.click(self.ADD_NEW_ADDRESS_BUTTON)
    
    def check_address_cancel_button_enabled(self):
        return self.is_enabled(self.ADDRESS_CANCEL_BUTTON)
    
    def check_address_previous_button_enabled(self):
        return self.is_enabled(self.ADDRESS_PREVIOUS_BUTTON)
    
    def check_address_save_button_enabled(self):
        return self.is_enabled(self.ADDRESS_SAVE_BUTTON)
    
    def check_address_next_button_enabled(self):
        return self.is_enabled(self.ADDRESS_NEXT_BUTTON)
    
    def get_address_title_error_text(self):
        return self.get_error_text(self.ERROR_ADDRESS_TITLE)
    
    def get_address_street_error_text(self):
        return self.get_error_text(self.ERROR_STREET)
    
    def get_house_no_error_text(self):
        return self.get_error_text(self.ERROR_HOUSE_NO)
    
    def get_description_error_text(self):
        return self.get_error_text(self.ERROR_DESCRIPTION)

    def get_address_list(self):
        return self.get_elemets_from_locator(self.ADDRESS_LIST_CONTROL)

    
    def add_new_address(self, title, city, street, house_no, description):
        #self.click(self.ADD_NEW_ADDRESS_BUTTON)
        self.send_keys(self.ADDRESS_TITLE, title)
        self.send_keys(self.CITY, city)
        self.send_keys(self.STREET, street)
        self.send_keys(self.HOUSE_NUMBER, house_no)
        self.send_keys(self.ADDRESS_DESCRIPTION, description)
        self.click(self.ADDRESS_SAVE_BUTTON)

    def check_add_new_address(self, title, city, street, house_no, description):
        self.click(self.ADD_NEW_ADDRESS_BUTTON)
        self.send_keys(self.ADDRESS_TITLE, title)
        self.send_keys(self.CITY, city)
        self.send_keys(self.STREET, street)
        self.send_keys(self.HOUSE_NUMBER, house_no)
        self.send_keys(self.ADDRESS_DESCRIPTION, description)

    def click_next_button_on_address_interface(self):
        self.click(self.ADDRESS_INTERFACE_NEXT_BUTTON)

    def go_to_contact_info(self):
        self.force_click_next_button()

    # def force_click_next_button(self):
 
    #     next_button = self.driver.find_element(*self.ADDRESS_NEXT_BUTTON)
    #     self.driver.execute_script("arguments[0].click();", next_button)

    def fill_contact_info(self, email, mobile_phone, **kwargs):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.MOBILE_PHONE, mobile_phone)
        if kwargs.get("home_phone"):
            self.send_keys(self.HOME_PHONE, kwargs["home_phone"])
        if kwargs.get("fax"):
            self.send_keys(self.FAX, kwargs["fax"])

    def check_contact_medium_create_button_enabled(self):
        return self.is_enabled(self.CREATE_BUTTON) 
    
    def click_create_customer(self):
        self.click(self.CREATE_BUTTON)

    def check_contact_medium_previous_button_enabled(self):
        return self.is_enabled(self.CONTACT_MEDIUM_PREVIOUS_BUTTON)
    
    def get_mobile_phone_error_text(self):
        return self.get_error_text(self.ERROR_MOBILE_PHONE)
    
    def get_email_error_text(self):
        return self.get_error_text(self.ERROR_EMAIL)
    
    def get_customer_with_this_natid_already_exists_error_text(self):
        return self.get_error_text(self.ERROR_ALREADY_EXISTS)