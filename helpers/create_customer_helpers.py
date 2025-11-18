from pages.customercreation_page import CustomerCreationPage
from data.customer_create_data import CreateCustomerData

# address bilgilerini doldurma fonksiyonu
def fill_and_submit_address_info(driver, wait):

    customer_page = CustomerCreationPage(driver, wait)
    customer_page.click_add_new_address_button()
    customer_page.add_new_address(
            CreateCustomerData.VALID_TITLE,
            CreateCustomerData.VALID_CITY,
            CreateCustomerData.VALID_STREET,
            CreateCustomerData.VALID_HOUSE_NO,
            CreateCustomerData.VALID_DESCRIPTION
        )
    customer_page.click_next_button_on_address_interface()

    return customer_page

# demografik bilgileri doldurma fonksiyonu
def fill_and_submit_demographic_info(driver, wait, nat_id):

    customer_page = CustomerCreationPage(driver, wait)

    customer_page.open_customer_creation()

    customer_page.fill_demographic_info(
            CreateCustomerData.VALID_FIRST_NAME,
            CreateCustomerData.VALID_LAST_NAME,
            CreateCustomerData.VALID_DATE_OF_BIRTH,
            CreateCustomerData.GENDER_MALE,
            nat_id
        )
    
    customer_page.submit_demographic()

    return customer_page