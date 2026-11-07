import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from utils.test_data import PRODUCTS, PRODUCT_NAMES

pytestmark = pytest.mark.ui


def test_add_and_remove_updates_cart_badge(inventory):
    inventory.add(PRODUCTS[0])
    expect(inventory.badge).to_have_text("1")
    inventory.remove(PRODUCTS[0])
    expect(inventory.badge).to_have_count(0)


@pytest.mark.smoke
def test_two_added_products_appear_in_cart(inventory, page):
    for product in PRODUCTS:
        inventory.add(product)
    expect(inventory.badge).to_have_text("2")
    inventory.open_cart()
    cart = CartPage(page)
    expect(cart.items).to_have_count(2)
    expect(cart.names).to_have_text(list(PRODUCT_NAMES))
