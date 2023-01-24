from fastapi.testclient import TestClient
from main import app


# Instantiate the testing client with our app.
client = TestClient(app)

# Test "/" endpoint
def test_api_locally_get_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}


# Test POST method with "/items" endpoint
def test_create_item():
    r = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"name": "Air Jordan 1", "tags": "shoes", "item_id": 1},
    )
    assert r.status_code == 200
    assert r.json() == {
        "name": "Air Jordan 1",
        "tags": "shoes",
        "item_id": 1
    }


# Test GET method with "/item/1?count=10" endpoint
def test_get_item():
    r = client.get(
        "/items/1?count=10",
        headers={"X-Token": "coneofsilence"},
    )
    assert r.status_code == 200
