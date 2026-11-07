import pytest

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_products_returns_200_and_json(products_response):
    assert products_response.status_code == 200
    assert "application/json" in products_response.headers.get("Content-Type", "")
    data = products_response.json()
    assert isinstance(data, dict)
    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0


def test_every_product_has_required_fields(products):
    for product in products:
        assert {"id", "title", "price"} <= product.keys()
        assert type(product["id"]) is int
        assert isinstance(product["title"], str) and product["title"].strip()
        assert type(product["price"]) in (int, float)


def test_every_product_price_is_positive(products):
    assert all(product["price"] > 0 for product in products)


def test_limit_restricts_number_of_products(api, api_url):
    response = api.get(f"{api_url}/products", params={"limit": 3}, timeout=20)
    assert response.status_code == 200
    data = response.json()
    assert 0 < len(data["products"]) <= 3
    assert data["limit"] == 3


def test_single_product_returns_requested_id(api, api_url):
    response = api.get(f"{api_url}/products/1", timeout=20)
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_unknown_product_returns_404(api, api_url):
    response = api.get(f"{api_url}/products/999999", timeout=20)
    assert response.status_code == 404
    assert "not found" in response.json()["message"].lower()
