import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from utils.login_json_parser import get_login_scenarios
from typing import List, Tuple, Any

@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    yield wait

@pytest.fixture(scope='session')
def ui_validation_params() -> List[Tuple[Any, Any, Any, Any]]:

    ui_data_list = get_login_scenarios('ui_validations')

    ui_params_list = []
    # 💡 HATA AYIKLAMA BAŞLANGICI
    print("\n--- UI Validation Fixture Hata Ayıklama ---")
    

    for key in ui_data_list:
        username = key.get('username_input')
        password = key.get('password_input')
        scenario_name = key.get('scenario_name')
        excepted_value = None
        excepted_state = key.get('expected_state')
        excepted_attribute = key.get('expected_attribute')

        if excepted_state is not None:
            excepted_value = excepted_state

        elif excepted_attribute is not None:
            excepted_value = excepted_attribute
        
        if excepted_value is not None:
            ui_params_list.append((username, password, scenario_name, excepted_value))

    return ui_params_list

@pytest.fixture(scope='session')
def negative_login_params() -> List[Tuple[Any, Any, Any, Any]]:

    negative_data_list = get_login_scenarios('negative_login_scenarios')

    negative_params_list = []

    for key in negative_data_list:
        username = key.get('username')
        password = key.get('password')
        scenario_name = key.get('scenario_name')
        excepted_error = key.get('expected_error')

        if excepted_error is not None:
            negative_params_list.append((username, password, scenario_name, excepted_error))

    return negative_params_list

@pytest.fixture(scope='session')
def positive_login_params() -> List[Tuple[Any, Any, Any]]:

    positive_data_list = get_login_scenarios('positive_login_scenarios')

    positive_params_list = []

    for key in positive_data_list:
        username = key.get('username')
        password = key.get('password')
        scenario_name = key.get('scenario_name')

        positive_params_list.append((username, password, scenario_name))

    return positive_params_list
