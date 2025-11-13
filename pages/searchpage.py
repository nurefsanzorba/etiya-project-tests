from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    NATID_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='natId']")
    CUSTOMERID_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='customerNumber']")
    ACCOUNTNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='accountNumber']")
    GSMNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='mobilePhone']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='lastName']")
    ORDERNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='orderNumber']")
    SEARCH_BUTTON = (By.NAME, "search-btn")
    CLEAR_BUTTON = (By.NAME,"clear-btn")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "div.bg-red-500.text-white.text-xs.mt-1.p-1.rounded")

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def load(self, url):
        return super().load(url)
    
    def search_with_11_digit_nat_id(self, natid):
        self.send_keys(self.NATID_INPUT, natid)
        self.click(self.SEARCH_BUTTON)


    def enter_nat_id_only(self, natid):
        self.send_keys(self.NATID_INPUT, natid)

    def enter_customer_id_only(self, customerid):
        self.send_keys(self.CUSTOMERID_INPUT, customerid)

    def enter_account_number_only(self, accountnumber):
        self.send_keys(self.ACCOUNTNUMBER_INPUT, accountnumber)

    def enter_gsm_number_only(self, gsmnumber):
        self.send_keys(self.GSMNUMBER_INPUT, gsmnumber)

    def enter_order_number_only(self, ordernumber):
        self.send_keys(self.ORDERNUMBER_INPUT, ordernumber)

    def enter_first_name_only(self, firstname):
        self.send_keys(self.FIRSTNAME_INPUT, firstname)

    def enter_last_name_only(self, lastname):
        self.send_keys(self.LASTNAME_INPUT, lastname)


    def is_search_button_enabled(self):
        return self.is_enabled(self.SEARCH_BUTTON)


    def get_input_disabled_state(self, locator):
        """True dönerse alan devre dışı (disabled) demektir."""
        return not self.is_enabled(locator)

    def check_fields_disabled_after_natid(self):
        fields = [self.CUSTOMERID_INPUT, self.ACCOUNTNUMBER_INPUT, self.GSMNUMBER_INPUT, self.ORDERNUMBER_INPUT]
        return self.check_fields_disabled_after(fields)

    def check_fields_disabled_after_customerid(self):
        fields = [self.NATID_INPUT, self.ACCOUNTNUMBER_INPUT, self.GSMNUMBER_INPUT, self.ORDERNUMBER_INPUT]
        return self.check_fields_disabled_after(fields)

    def check_fields_disabled_after_accountnumber(self):
        fields = [self.NATID_INPUT, self.CUSTOMERID_INPUT, self.GSMNUMBER_INPUT, self.ORDERNUMBER_INPUT]
        return self.check_fields_disabled_after(fields)

    def check_fields_disabled_after_gsmnumber(self):
        fields = [self.NATID_INPUT, self.ACCOUNTNUMBER_INPUT, self.CUSTOMERID_INPUT, self.ORDERNUMBER_INPUT]
        return self.check_fields_disabled_after(fields)

    def check_fields_disabled_after_ordernumber(self):
        fields = [self.NATID_INPUT, self.ACCOUNTNUMBER_INPUT, self.GSMNUMBER_INPUT, self.CUSTOMERID_INPUT]
        return self.check_fields_disabled_after(fields)
    

    def get_error_message(self):
        return self.get_error_text(self.ERROR_CONTAINER)
    
    def click_clear_button(self):
        self.click(self.CLEAR_BUTTON)


    def are_all_fields_empty(self):
        fields = [
            self.NATID_INPUT,
            self.CUSTOMERID_INPUT,
            self.ACCOUNTNUMBER_INPUT,
            self.GSMNUMBER_INPUT,
            self.FIRSTNAME_INPUT,
            self.LASTNAME_INPUT,
            self.ORDERNUMBER_INPUT
    ]
    
        for field in fields:
            try:
                self.wait.until(lambda d: self.get_attribute(field, "value") == "")
            except:
                return False
        return True
