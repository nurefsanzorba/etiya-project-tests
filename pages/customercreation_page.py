from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CustomerCreationPage(BasePage):

    # === Locators ===
    CREATE_CUSTOMER_BUTTON = (By.ID, "createCustomerBtn")
    CANCEL_BUTTON = (By.ID, "cancelBtn")

    # Demographic info fields
    FIRST_NAME = (By.ID, "firstName")
    MIDDLE_NAME = (By.ID, "middleName")
    LAST_NAME = (By.ID, "lastName")
    DOB = (By.ID, "birthDate")
    GENDER = (By.ID, "genderDropdown")
    FATHER_NAME = (By.ID, "fatherName")
    MOTHER_NAME = (By.ID, "motherName")
    NATIONALITY_ID = (By.ID, "nationalityId")
    NEXT_BUTTON = (By.ID, "nextBtn")
    WARNING_MSG = (By.CSS_SELECTOR, ".warning-message")

    # Address Info
    ADD_NEW_ADDRESS_BUTTON = (By.ID, "addNewAddressBtn")
    ADDRESS_TITLE = (By.ID, "addressTitle")
    CITY = (By.ID, "city")
    STREET = (By.ID, "street")
    HOUSE_NUMBER = (By.ID, "houseNumber")
    ADDRESS_DESCRIPTION = (By.ID, "addressDescription")
    ADDRESS_SAVE_BUTTON = (By.ID, "saveAddressBtn")
    ADDRESS_NEXT_BUTTON = (By.ID, "nextAddressBtn")
    PREVIOUS_BUTTON = (By.ID, "previousBtn")

    # Contact Info
    EMAIL = (By.ID, "email")
    HOME_PHONE = (By.ID, "homePhone")
    MOBILE_PHONE = (By.ID, "mobilePhone")
    FAX = (By.ID, "fax")
    CREATE_BUTTON = (By.ID, "createBtn")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".email-error")

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

    def submit_demographic(self):
        self.click(self.NEXT_BUTTON)

    def check_duplicate_warning(self):
        return self.get_text(self.WARNING_MSG)

    def add_new_address(self, title, city, street, house_no, description):
        self.click(self.ADD_NEW_ADDRESS_BUTTON)
        self.send_keys(self.ADDRESS_TITLE, title)
        self.send_keys(self.CITY, city)
        self.send_keys(self.STREET, street)
        self.send_keys(self.HOUSE_NUMBER, house_no)
        self.send_keys(self.ADDRESS_DESCRIPTION, description)
        self.click(self.ADDRESS_SAVE_BUTTON)

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
