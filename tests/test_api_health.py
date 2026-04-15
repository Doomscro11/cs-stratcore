"""Executable foundation tests for API import and health behavior."""

from importlib import import_module

from fastapi.testclient import TestClient

from cs_stratcore.api.main import app


def test_root_package_importable() -> None:
    module = import_module("cs_stratcore")
    assert hasattr(module, "__version__")


def test_fastapi_app_importable() -> None:
    module = import_module("cs_stratcore.api.main")
    assert hasattr(module, "app")


def test_health_endpoint_returns_expected_payload() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"service": "cs-stratcore", "status": "ok"}
