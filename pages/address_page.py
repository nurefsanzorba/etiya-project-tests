from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage  

class AddressPage(BasePage):

    #LOCATORS 
    ADDRESS_TAB = (By.ID, "address-tab")
    ADD_NEW_BUTTON = (By.ID, "add-new-address-btn")
    SAVE_BUTTON = (By.ID, "save-address-btn")

    # Pop-up fields
    ADDRESS_TITLE_INPUT = (By.ID, "address-title")
    CITY_INPUT = (By.ID, "city")
    STREET_INPUT = (By.ID, "street")
    HOUSE_NUMBER_INPUT = (By.ID, "house-number")
    DESCRIPTION_INPUT = (By.ID, "description")

    # Address list
    ADDRESS_LIST = (By.CSS_SELECTOR, ".address-card")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".address-card .edit-btn")
    PRIMARY_RADIO = (By.CSS_SELECTOR, ".address-card .primary-radio")

    #  METHODS 
    def open_address_tab(self):
        self.click(self.ADDRESS_TAB)

    def open_add_address_popup(self):
        self.click(self.ADD_NEW_BUTTON)

    def fill_address_form(self, title, city, street, house, description):
        self.send_keys(self.ADDRESS_TITLE_INPUT, title)
        self.send_keys(self.CITY_INPUT, city)
        self.send_keys(self.STREET_INPUT, street)
        self.send_keys(self.HOUSE_NUMBER_INPUT, house)
        self.send_keys(self.DESCRIPTION_INPUT, description)

    def save_address(self):
        self.click(self.SAVE_BUTTON)

    def is_save_enabled(self):
        return self.is_enabled(self.SAVE_BUTTON)

    def edit_address(self, index=0):
        cards = self.driver.find_elements(*self.ADDRESS_LIST)
        cards[index].find_element(*self.EDIT_BUTTON).click()

    def select_primary_address(self, index=0):
        cards = self.driver.find_elements(*self.ADDRESS_LIST)
        radio = cards[index].find_element(*self.PRIMARY_RADIO)
        if not radio.is_selected():
            radio.click()

    def get_address_cards_count(self):
        return len(self.driver.find_elements(*self.ADDRESS_LIST))