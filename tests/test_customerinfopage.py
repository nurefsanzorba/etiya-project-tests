import pytest
from pages.customerinfo_page import CustomerInfoPage

@pytest.mark.usefixtures("driver", "wait", "login")
class TestCustomerInfoPage:

    CUSTOMER_ID = "CUST-2025-865834"

    def test_update_customer_info_success(self, driver, wait):
        customer_page = CustomerInfoPage(driver, wait)
        customer_page.open_customer_info(self.CUSTOMER_ID)
        customer_page.click_edit()

        customer_page.fill_customer_info(
            firstName="John",
            lastName="Doe",
            birthDate="1980-01-01",
            gender="Male",
            nationalityId="98765432101"
        )

        assert customer_page.is_save_enabled(), "Save button should be enabled"
        customer_page.click_save()

        assert "Customer Info" in driver.title

    def test_update_customer_info_duplicate_nationality(self, driver, wait):
        customer_page = CustomerInfoPage(driver, wait)
        customer_page.open_customer_info(self.CUSTOMER_ID)
        customer_page.click_edit()

        customer_page.fill_customer_info(
            firstName="Jane",
            lastName="Smith",
            birthDate="1990-05-15",
            gender="Female",
            nationalityId="11111111111"  # Already exists
        )

        customer_page.click_save()
        warning = customer_page.get_warning_text()
        assert warning == "A customer already exists with this Nationality ID"

    def test_delete_customer_with_active_product(self, driver, wait):
        customer_page = CustomerInfoPage(driver, wait)
        customer_page.open_customer_info(self.CUSTOMER_ID)
        customer_page.click_delete()
        customer_page.confirm_delete()

        warning = customer_page.get_delete_warning()
        assert warning == "Since the customer has active products, the customer cannot be deleted."

    def test_delete_customer_success(self, driver, wait):
        customer_page = CustomerInfoPage(driver, wait)
        customer_page.open_customer_info(self.CUSTOMER_ID)
        customer_page.click_delete()
        customer_page.confirm_delete()

        assert "Customer Search" in driver.title
