from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    # --- Locator'lar ---
    NATID_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='natId']")
    CUSTOMERID_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='customerId']")
    ACCOUNTNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='accountNumber']")
    GSMNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='gsmNumber']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='lastName']")
    ORDERNUMBER_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='orderNumber']")
    SEARCH_BUTTON = (By.NAME, "search-btn")

    def __init__(self, wait, driver):
        super().__init__(wait, driver)

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
