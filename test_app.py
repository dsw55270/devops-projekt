from app import app

def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "API dziala"

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_add():
    client = app.test_client()
    resp = client.get("/add/2/3")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5
