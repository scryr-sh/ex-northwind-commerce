from fastapi.testclient import TestClient

from northwind_api.main import app


client = TestClient(app)


def test_catalog_returns_products():
    response = client.get("/catalog")

    assert response.status_code == 200
    products = response.json()
    assert products[0]["sku"] == "BEV-CHAI-48"
    assert "unitPriceCents" in products[0]


def test_checkout_creates_stubbed_payment_intent():
    response = client.post(
        "/checkout",
        json={
            "accountId": "northwind-wholesale",
            "currency": "usd",
            "shippingSpeed": "expedited",
            "lines": [{"productId": "chai-001", "quantity": 2}],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["paymentIntentId"].startswith("pi_stub_")
    assert body["status"] == "stubbed"
    assert body["riskScore"] > 0


def test_checkout_rejects_unknown_product():
    response = client.post(
        "/checkout",
        json={
            "accountId": "northwind-wholesale",
            "lines": [{"productId": "missing", "quantity": 1}],
        },
    )

    assert response.status_code == 404
