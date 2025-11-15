import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from pages.loginpage import LoginPage
from pages.customercreation_page import CustomerCreationPage

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

# basarılı giriş için eklenen fixture
@pytest.fixture
def succes_login(driver, wait):
    """
    Login işlemini yapan fixture.
    Testlerde @pytest.mark.usefixtures("login") olarak kullanılır.
    """
    login_page = LoginPage(driver, wait)
    login_page.load_login()
    login_page.login("selenium-test", "s3l3n1um-t3st")
    yield driver

@pytest.fixture
def succes_demographic_info(succes_login, wait):
    driver = succes_login
    customer_page = CustomerCreationPage(driver, wait)

    customer_page.open_customer_creation()

    customer_page.fill_demographic_info(
            first_name="Ali",
            last_name="Yılmaz",
            dob="01/01/1990",
            gender="Male",
            nationality_id="12345678900"
        )
    
    customer_page.submit_demographic()

    yield driver

