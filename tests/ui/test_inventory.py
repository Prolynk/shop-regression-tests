from decimal import Decimal
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_inventory_contains_six_products(inventory):
    expect(inventory.items).to_have_count(6)


def test_prices_sort_low_to_high(inventory):
    inventory.sort("lohi")
    expect(inventory.page.get_by_test_id("product-sort-container")).to_have_value("lohi")
    prices = [Decimal(x.removeprefix("$")) for x in inventory.prices.all_text_contents()]
    assert len(prices) == 6
    assert prices == sorted(prices)


def test_names_sort_z_to_a(inventory):
    inventory.sort("za")
    expect(inventory.page.get_by_test_id("product-sort-container")).to_have_value("za")
    names = inventory.names.all_text_contents()
    assert len(names) == 6
    assert names == sorted(names, reverse=True)
