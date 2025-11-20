import os
from app import app  # this comes from app/__init__.py


def test_root_default_target():
    """Root (/) should use the default TARGET."""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello LIVE DEMO 101!" in response.data


def test_root_custom_target(monkeypatch):
    """Root (/) should respect TARGET env var."""
    monkeypatch.setenv("TARGET", "Mikael")

    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello Mikael!" in response.data


def test_healthz_endpoint():
    """Liveness probe should return ok/alive."""
    client = app.test_client()
    response = client.get("/healthz")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["message"] == "alive"


def test_ready_endpoint():
    """Readiness probe should return ok/ready."""
    client = app.test_client()
    response = client.get("/ready")

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["message"] == "ready"
