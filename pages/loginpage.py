from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = BasePage.BASE_URL + "login"
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    EYE_ICON = (By.CSS_SELECTOR, "button[class='eye-btn']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='btn-login']")
    LOGIN_ERROR = (By.CSS_SELECTOR, "p[name='login-error']")


    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def load_login(self):
        self.load(self.LOGIN_URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_text(self):
        return self.get_text(self.LOGIN_ERROR)
    
    def eye_click(self):
        self.click(self.EYE_ICON)

    def type_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def type_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT)).send_keys(username)
    def read_password_type_attribute(self):
        return self.get_attribute(self.PASSWORD_INPUT, "type")
    
    def login_button_control(self):
        return self.is_enabled(self.LOGIN_BUTTON)
    


    