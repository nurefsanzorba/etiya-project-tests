from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from pages.loginpage import LoginPage

class CustomerInfoPage(BasePage):

    EDIT_BUTTON = (By.CSS_SELECTOR, "button.px-6.py-2.border-gray-300")
    DELETE_CUSTOMER_BUTTON = (By.XPATH, "//button[text()='Delete Customer']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")
    CANCEL_DELETE_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    DELETE_POPUP = (By.CSS_SELECTOR, "div.bg-white.rounded-lg.shadow-xl.p-6")
    WARNING_MESSAGE = (By.CSS_SELECTOR, "p.text-gray-700")

    FIRST_NAME_INPUT = (By.ID, "firstName")
    MIDDLE_NAME_INPUT = (By.ID, "middleName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    DOB_INPUT = (By.ID, "birthDate")
    GENDER_SELECT = (By.ID, "gender")
    FATHER_NAME_INPUT = (By.ID, "fatherName")
    MOTHER_NAME_INPUT = (By.ID, "motherName")
    NATIONALITY_ID_INPUT = (By.ID, "nationalityId")
    
    def open_customer_info(self, customer_id):
        self.load(f"http://localhost:4200/b2c/customer-info/{customer_id}")

    def click_edit(self):
        self.wait.until(EC.visibility_of_element_located(self.EDIT_BUTTON))
        self.click(self.EDIT_BUTTON)
    
    def fill_customer_info(self, firstName=None, middleName=None, lastName=None,
                           birthDate=None, gender=None, fatherName=None,
                           motherName=None, nationalityId=None):

        if firstName is not None:
            self.send_keys(self.FIRST_NAME_INPUT, firstName)
        if middleName is not None:
            self.send_keys(self.MIDDLE_NAME_INPUT, middleName)
        if lastName is not None:
            self.send_keys(self.LAST_NAME_INPUT, lastName)
        if birthDate is not None:
            self.send_keys(self.DOB_INPUT, birthDate)
        if gender is not None:
            self.send_keys(self.GENDER_SELECT, gender)
        if fatherName is not None:
            self.send_keys(self.FATHER_NAME_INPUT, fatherName)
        if motherName is not None:
            self.send_keys(self.MOTHER_NAME_INPUT, motherName)
        if nationalityId is not None:
            self.send_keys(self.NATIONALITY_ID_INPUT, nationalityId)
    
    def is_save_enabled(self):
        return self.is_enabled(self.SAVE_BUTTON)
    
    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.click(self.SAVE_BUTTON)
    
    def get_warning_text(self):
        return self.get_text(self.WARNING_MESSAGE)
    
    def click_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_CUSTOMER_BUTTON))
        self.click(self.DELETE_CUSTOMER_BUTTON)
    
    def confirm_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON))
        self.click(self.CONFIRM_DELETE_BUTTON)
    
    def cancel_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_DELETE_BUTTON))
        self.click(self.CANCEL_DELETE_BUTTON)
    
    def get_delete_warning(self):
        return self.get_text(self.WARNING_MESSAGE)
