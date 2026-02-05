import json
import os
import pytest
from pageObjects.LoginPage import LoginPage


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
test_data_path = os.path.join(BASE_DIR, "data", "test_e2e.json")

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.negative
def test_invalid_login(browserInstance):
    """
    Verifies that user cannot login with invalid credentials
    """
    login_page = LoginPage(browserInstance)
    login_page.login("wronguser", "wrongpassword")

    assert "Incorrect" in browserInstance.page_source

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    login_page = LoginPage(driver)
    shop_page = login_page.login(
        test_list_item["userEmail"],
        test_list_item["userPassword"]
    )

    shop_page.add_product_to_card(test_list_item["productName"])
    checkout_page = shop_page.goToCard()

    checkout_page.checkout()
    checkout_page.enter_delivery_address("ind")
    checkout_page.validate_order()
