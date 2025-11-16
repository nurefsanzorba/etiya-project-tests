from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    BASE_URL = "http://localhost:4200/"

    def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait


    def load(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)
    
    def is_enabled(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_enabled()
    
    def can_click_search_button(self):
       try:
           self.driver.find_element(*self.SEARCH_BUTTON).click()
           return True
       except:
           return False
       
    
    def check_fields_disabled_after(self, fields_to_check):
        """Belirli bir alan doldurulduktan sonra kontrol edilecek alanları döner."""
        return [field for field in fields_to_check if self.get_input_disabled_state(field)]
    

    def get_error_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def clear_input_field(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()