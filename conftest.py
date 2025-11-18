import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from pages.loginpage import LoginPage
from pages.searchpage import SearchPage
from pages.customerinfo_page import CustomerInfoPage
from data.login_data import LoginConstants
from data.customer_create_data import CreateCustomerData
from helpers import create_customer_helpers as CH
from helpers import screenshot_helpers as SH


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if 'driver' in item.funcargs:
            driver = item.funcargs['driver']

            status = "PASSED" if report.passed else "FAILED" if report.failed else "OTHER"

            if report.outcome in ("passed", "failed"):
                SH.save_screenshot_on_teardown(driver, item.nodeid, status)

# basarılı giriş için eklenen fixture
@pytest.fixture
def succes_login(driver, wait):
    login_page = LoginPage(driver, wait)
    login_page.load_login()
    login_page.login(LoginConstants.VALID_USERNAME, LoginConstants.VALID_PASSWORD)
    yield driver

# başarılı demogrophic info zincir fixture
@pytest.fixture
def succes_demographic_info(succes_login, wait):
    driver = succes_login

    customer_page = CH.fill_and_submit_demographic_info(driver, wait, CreateCustomerData.VALID_NAT_ID)

    yield customer_page

# başarısız demographic info zincir fixture
@pytest.fixture
def exists_demographic_info(succes_login, wait):
    driver = succes_login
    
    customer_page = CH.fill_and_submit_demographic_info(driver, wait, CreateCustomerData.EXIST_NAT_ID)

    yield customer_page

# mevcut nat_id ile doğru adres bilgilerinin gönderildiği fixture
@pytest.fixture
def exists_demographic_info_success_address(exists_demographic_info, wait):
    driver = exists_demographic_info
    
    customer_page = CH.fill_and_submit_address_info(driver, wait)
    
    yield customer_page

# yeni kayıt ile doğru adres bilgilerinin gönderildiği fixture
@pytest.fixture
def succes_address_info(succes_demographic_info, wait):
    driver = succes_demographic_info

    customer_page = CH.fill_and_submit_address_info(driver, wait)
    
    yield customer_page


@pytest.fixture
def open_customer_info_page(succes_login,wait):
    driver = succes_login
    customer_search_page= SearchPage(driver,wait)
    customer_search_page.search_with_11_digit_nat_id("48528397800")
    customer_search_page.click_first_customer_id_button()
    yield driver
    

# valid nat id fixture
@pytest.fixture(scope="session")
def valid_nat_id():
    return CreateCustomerData.VALID_NAT_ID

# exists nat id fixture
@pytest.fixture(scope="session")
def exitst_nat_id():
    return CreateCustomerData.EXIST_NAT_ID

