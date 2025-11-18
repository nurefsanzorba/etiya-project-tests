import pytest
from pages.address_page import AddressPage

@pytest.mark.ui
def test_add_address(driver, wait):
    page = AddressPage(driver, wait)
    page.load(page.BASE_URL)

    # ACC1: Open Address tab
    page.open_address_tab()

    # ACC2: Open add new address popup
    page.open_add_address_popup()

    # ACC3: Save should be disabled initially
    assert not page.is_save_enabled()

    # Fill all mandatory fields
    page.fill_address_form(
        title="Home",
        city="Istanbul",
        street="Istiklal Street",
        house="12A",
        description="Near the park"
    )

    # ACC4: Save should be enabled
    assert page.is_save_enabled()

    # Click save
    page.save_address()

    # ACC5: Verify new address appears
    assert page.get_address_cards_count() > 0

@pytest.mark.usefixtures("driver", "wait")
class TestAddressUpdate:

    # ACC1 – Navigate to Address Screen
    def test_ACC1_user_navigates_to_address_screen(self, driver, wait):
        page = AddressPage(driver, wait)

        page.load(page.BASE_URL + "/addresses")  # Navigasyon
        assert "addresses" in driver.current_url

    # ACC2 – System displays all saved addresses
    def test_ACC2_display_saved_addresses(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()
        assert count > 0, "Address list is empty but should contain items."

    # ACC3 – User can select a primary address
    def test_ACC3_user_can_set_primary_address(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()
        assert count > 0

        page.select_primary_address(0)

        # Verify selected
        cards = driver.find_elements(*page.ADDRESS_LIST)
        radio = cards[0].find_element(*page.PRIMARY_RADIO)
        assert radio.is_selected(), "Primary radio did not get selected."

    # ACC4 – If only one address exists, primary radio is selected and locked
    def test_ACC4_primary_radio_locked_when_single_address(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()

        if count == 1:
            cards = driver.find_elements(*page.ADDRESS_LIST)
            radio = cards[0].find_element(*page.PRIMARY_RADIO)

            assert radio.is_selected(), "Single address should be selected as primary."
            assert radio.get_attribute("disabled") in ["true", "disabled"], \
                "Primary address radio should be disabled for a single address."

    # ACC5 – User can open edit popup
    def test_ACC5_user_can_open_edit_screen(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        page.edit_address(0)

        # Edit popup expected field check
        assert wait.until(EC.visibility_of_element_located(page.CITY_INPUT))

    # ACC6 – Edit screen opens with pre-filled data
    def test_ACC6_edit_form_prefilled(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        page.edit_address(0)

        city_value = page.get_attribute(page.CITY_INPUT, "value")
        assert city_value is not None and city_value != "", \
            "City field should be pre-filled on edit screen."

    # ACC7 – User can modify fields, mandatory validation applies
    def test_ACC7_mandatory_validation(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        page.edit_address(0)

        # Clear mandatory fields
        page.send_keys(page.CITY_INPUT, "")
        page.send_keys(page.STREET_INPUT, "")
        page.send_keys(page.DESCRIPTION_INPUT, "")

        assert not page.is_save_enabled(), "Save should be disabled when mandatory fields are empty."

    # ACC8 – Save disabled until mandatory fields are filled
    def test_ACC8_save_button_disabled_until_all_filled(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        page.edit_address(0)

        # Step 1: Clear everything
        page.send_keys(page.CITY_INPUT, "")
        page.send_keys(page.STREET_INPUT, "")
        page.send_keys(page.DESCRIPTION_INPUT, "")

        assert not page.is_save_enabled()

        # Step 2: Fill partially
        page.send_keys(page.CITY_INPUT, "New City")
        assert not page.is_save_enabled()

        # Step 3: Fill ALL mandatory
        page.send_keys(page.STREET_INPUT, "New Street")
        page.send_keys(page.DESCRIPTION_INPUT, "Updated desc")

        assert page.is_save_enabled(), "Save should be enabled after all mandatory fields are filled."

    # ACC9 – Save updates and persists address info
    def test_ACC9_save_updates_address(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        page.edit_address(0)

        updated_value = "CITY-UPDATED-123"
        page.send_keys(page.CITY_INPUT, updated_value)
        page.save_address()

        # Verify updated list UI
        cards = driver.find_elements(*page.ADDRESS_LIST)
        assert updated_value in cards[0].text, \
            "Updated city value is not reflected in the address list."

#FR 5.3
    # ACC1 – User navigates to Address screen
    def test_ACC1_navigate_to_address_screen(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")
        assert "/addresses" in driver.current_url

    # ACC2 – System displays saved addresses
    def test_ACC2_display_saved_addresses(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()
        assert count > 0, "No addresses displayed on Address screen!"

    # ACC3 – Delete disabled if only 1 address
    def test_ACC3_delete_disabled_if_single_address(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()

        if count == 1:
            enabled = page.is_delete_button_enabled(index=0)
            assert enabled is False, "Delete button should be disabled when only one address exists."

    # ACC4 – Delete enabled if 2+ addresses
    def test_ACC4_delete_enabled_if_multiple_addresses(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        count = page.get_address_cards_count()

        if count >= 2:
            enabled = page.is_delete_button_enabled(index=0)
            assert enabled is True, "Delete button should be enabled when there are 2 or more addresses."

    # ACC5 & ACC6 – User can delete an address + Confirmation popup
    def test_ACC5_ACC6_user_can_delete_address(self, driver, wait):
        page = AddressPage(driver, wait)
        page.load(page.BASE_URL + "/addresses")

        initial_count = page.get_address_cards_count()
        assert initial_count >= 2, \
            "This test requires at least 2 addresses to validate delete functionality."

        # Initiate delete
        page.delete_address(index=0)

        # Verify confirmation popup appears
        wait.until(EC.visibility_of_element_located(page.DELETE_CONFIRM_YES))

        # Confirm delete
        page.confirm_delete()

        # After deletion, count must be decreased by 1
        final_count = page.get_address_cards_count()
        assert final_count == initial_count - 1, \
            "Address was not deleted after confirm YES click."
