from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    BASE_URL = "http://localhost:4200"

    def __init__(self, wait, driver):
        self.wait = wait
        self.driver = driver

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