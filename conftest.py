import os
import pytest
import requests
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USERNAME, PASSWORD


@pytest.fixture(scope="session", autouse=True)
def selectors(playwright):
    playwright.selectors.set_test_id_attribute("data-test")
    expect.set_options(timeout=10000)


@pytest.fixture
def login_page(page):
    page.goto(os.getenv("SHOP_URL", "https://www.saucedemo.com/"), wait_until="domcontentloaded")
    return LoginPage(page)


@pytest.fixture
def inventory(login_page, page):
    login_page.login(USERNAME, PASSWORD)
    result = InventoryPage(page)
    expect(page.get_by_test_id("title")).to_have_text("Products")
    return result


@pytest.fixture(scope="session")
def api():
    with requests.Session() as session:
        yield session


@pytest.fixture(scope="session")
def api_url():
    return os.getenv("PRODUCTS_API_URL", "https://dummyjson.com").rstrip("/")


@pytest.fixture(scope="session")
def products_response(api, api_url):
    return api.get(f"{api_url}/products", params={"limit": 0}, timeout=20)


@pytest.fixture(scope="session")
def products(products_response):
    products_response.raise_for_status()
    data = products_response.json()
    assert isinstance(data.get("products"), list)
    assert data["products"], "Products endpoint returned no products"
    return data["products"]


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # Playwright does not automatically inherit HTTP(S)_PROXY like requests does.
    proxy_url = os.getenv("PLAYWRIGHT_PROXY")
    if proxy_url:
        return {**browser_type_launch_args, "proxy": {"server": proxy_url}}
    return browser_type_launch_args
