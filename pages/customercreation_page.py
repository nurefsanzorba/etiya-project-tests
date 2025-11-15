from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CustomerCreationPage(BasePage):

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
    NEXT_BUTTON = (By.XPATH, "/html/body/app-root/app-b2c/div/div/app-create-customer/div/div/form/div/div[2]/button[2]")
    WARNING_MSG = (By.CSS_SELECTOR, ".text-red-500.text-xs.mt-1")
    WARNING_MSG2 = (By.CSS_SELECTOR, ".text-red-600.text-xs.mt-1")

    # Address Info
    ADD_NEW_ADDRESS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Add New Address']")
    ADDRESS_TITLE = (By.ID, "addressTitle")
    CITY = (By.ID, "city")
    STREET = (By.ID, "street")
    HOUSE_NUMBER = (By.ID, "houseNumber")
    ADDRESS_DESCRIPTION = (By.ID, "description")
    ADDRESS_SAVE_BUTTON = (By.XPATH, "//button[normalize-space(text())='Save']")
    ADDRESS_NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Next']")
    PREVIOUS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Previous']")

    # Contact Info
    EMAIL = (By.ID, "email")
    HOME_PHONE = (By.ID, "homePhone")
    MOBILE_PHONE = (By.ID, "mobilePhone")
    FAX = (By.ID, "fax")
    CREATE_BUTTON = (By.ID, "createBtn")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".email-error")

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

    
    def is_next_button_enabled(self):
        return self.is_enabled(self.ADDRESS_NEXT_BUTTON) 
    
    def is_save_button_enabled(self):
        return self.is_enabled(self.ADDRESS_SAVE_BUTTON) 

    def get_error_message_for_age(self):
        return self.get_error_text(self.WARNING_MSG)

    def get_error_message_for_natid(self):
        return self.get_error_text(self.WARNING_MSG2)    

    def submit_demographic(self):
        self.click(self.NEXT_BUTTON)

    def add_new_address(self, title, city, street, house_no, description):
        self.click(self.ADD_NEW_ADDRESS_BUTTON)
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
        
    def go_to_contact_info(self):
        self.click(self.ADDRESS_NEXT_BUTTON)

    def fill_contact_info(self, email, mobile_phone, **kwargs):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.MOBILE_PHONE, mobile_phone)
        if kwargs.get("home_phone"):
            self.send_keys(self.HOME_PHONE, kwargs["home_phone"])
        if kwargs.get("fax"):
            self.send_keys(self.FAX, kwargs["fax"])

    def create_customer(self):
        self.click(self.CREATE_BUTTON)
