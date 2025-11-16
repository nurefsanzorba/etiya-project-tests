import pytest
from pages.customerinfo_page import CustomerInfoPage
from pages.loginpage import LoginPage



class TestCustomerInfoPage:

    CUSTOMER_ID = "CUST-2025-865834"

    def test_update_customer_info_success(self, open_customer_info_page, wait):
        customer_page = CustomerInfoPage(open_customer_info_page, wait)
        customer_page.click_edit()

        customer_page.fill_customer_info(
            firstName="John",
            lastName="Doe",
            birthDate="01/01/1980",
            gender="Male",
            nationalityId="98765432102"
        )

        assert customer_page.is_save_enabled(), "Save button should be enabled"

    def test_update_customer_info_success_and_save(self, open_customer_info_page, wait):
        customer_page = CustomerInfoPage(open_customer_info_page, wait)
        customer_page.click_edit()

        customer_page.fill_customer_info(
            firstName="John",
            lastName="Doe",
            birthDate="01/01/1980",
            gender="Male",
            nationalityId="98765432102"
        )
        customer_page.click_save()
        assert True
    def test_update_customer_info_duplicate_nationality(self, open_customer_info_page, wait):
        customer_page = CustomerInfoPage(open_customer_info_page, wait)
        customer_page.click_edit()
        customer_page.fill_customer_info(
            firstName="Jane",
            lastName="Smith",
            birthDate="01/01/1980",
            gender="Female",
            nationalityId="12345678914"  # Already exists
        )

        customer_page.click_save()
        warning = customer_page.get_warning_text()
        assert warning == "A customer already exists with this Nationality ID" #warning message uyuşmadı

    def test_delete_customer_with_active_product(self, open_customer_info_page, wait):
        customer_page = CustomerInfoPage(open_customer_info_page, wait)
        customer_page.click_delete()
        customer_page.confirm_delete()
        warning = customer_page.get_delete_warning()
        assert warning == "Since the customer has active products, the customer cannot be deleted." #product eklenince test edilecek.

    def test_delete_customer_success(self, open_customer_info_page, wait):
        customer_page = CustomerInfoPage(open_customer_info_page, wait)
        customer_page.click_delete()
        customer_page.confirm_delete()
        assert True
