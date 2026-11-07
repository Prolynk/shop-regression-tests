import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import PRODUCTS

pytestmark = pytest.mark.ui


def start_checkout(inventory, page):
    inventory.add(PRODUCTS[0])
    inventory.open_cart()
    CartPage(page).checkout()
    return CheckoutPage(page)


@pytest.mark.smoke
def test_checkout_completes_order(inventory, page):
    checkout = start_checkout(inventory, page)
    checkout.continue_with()
    expect(page.get_by_test_id("inventory-item-name")).to_have_text("Sauce Labs Backpack")
    expect(page.get_by_test_id("subtotal-label")).to_have_text("Item total: $29.99")
    checkout.finish()
    expect(checkout.confirmation).to_have_text("Thank you for your order!")
    expect(page.get_by_test_id("shopping-cart-badge")).to_have_count(0)


def test_checkout_requires_first_name(inventory, page):
    checkout = start_checkout(inventory, page)
    checkout.continue_with(first_name="")
    expect(checkout.error).to_have_text("Error: First Name is required")
