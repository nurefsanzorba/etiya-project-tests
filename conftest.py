import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Tuple, Any
from pages.loginpage import LoginPage
from utils.login_json_parser import get_login_scenarios


@pytest.fixture(scope="session")
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture
def login(driver, wait):
    """
    Login işlemini yapan fixture.
    Testlerde @pytest.mark.usefixtures("login") olarak kullanılır.
    """
    login_page = LoginPage(driver, wait)
    login_page.load_login()
    login_page.login("mutlum123456", "123456")
    yield login_page


@pytest.fixture(scope="session")
def ui_validation_params() -> List[Tuple[Any, Any, Any, Any]]:
    """
    UI validation senaryolarını JSON'dan okur ve parametrik olarak döndürür.
    """
    ui_data_list = get_login_scenarios("ui_validations")
    ui_params_list = []

    print("\n--- UI Validation Fixture Hata Ayıklama ---")
    for key in ui_data_list:
        username = key.get("username_input")
        password = key.get("password_input")
        scenario_name = key.get("scenario_name")
        expected_state = key.get("expected_state")
        expected_attribute = key.get("expected_attribute")

        expected_value = expected_state if expected_state is not None else expected_attribute

        if expected_value is not None:
            ui_params_list.append((username, password, scenario_name, expected_value))

    return ui_params_list


@pytest.fixture(scope="session")
def negative_login_params() -> List[Tuple[Any, Any, Any, Any]]:
    """
    Negatif login senaryolarını JSON'dan okur.
    """
    negative_data_list = get_login_scenarios("negative_login_scenarios")
    negative_params_list = []

    for key in negative_data_list:
        username = key.get("username")
        password = key.get("password")
        scenario_name = key.get("scenario_name")
        expected_error = key.get("expected_error")

        if expected_error is not None:
            negative_params_list.append((username, password, scenario_name, expected_error))

    return negative_params_list


@pytest.fixture(scope="session")
def positive_login_params() -> List[Tuple[Any, Any, Any]]:
    """
    Pozitif login senaryolarını JSON'dan okur.
    """
    positive_data_list = get_login_scenarios("positive_login_scenarios")
    positive_params_list = []

    for key in positive_data_list:
        username = key.get("username")
        password = key.get("password")
        scenario_name = key.get("scenario_name")

        positive_params_list.append((username, password, scenario_name))

    return positive_params_list
