import re
import pytest
from playwright.sync_api import expect
from utils.test_data import USERNAME, PASSWORD

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login_opens_products(login_page, page):
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(page.get_by_test_id("title")).to_have_text("Products")


def test_wrong_password_is_rejected(login_page):
    login_page.login(USERNAME, "wrong-password")
    expect(login_page.error).to_have_text("Epic sadface: Username and password do not match any user in this service")


def test_locked_out_user_is_rejected(login_page):
    login_page.login("locked_out_user", PASSWORD)
    expect(login_page.error).to_have_text("Epic sadface: Sorry, this user has been locked out.")


@pytest.mark.parametrize("username,password,message", [
    ("", PASSWORD, "Username is required"),
    (USERNAME, "", "Password is required"),
])
def test_required_login_fields(login_page, username, password, message):
    login_page.login(username, password)
    expect(login_page.error).to_have_text(f"Epic sadface: {message}")


def test_logout_returns_to_login(inventory, page):
    inventory.logout()
    expect(page.get_by_test_id("login-button")).to_be_visible()
    expect(page.get_by_test_id("username")).to_be_empty()
