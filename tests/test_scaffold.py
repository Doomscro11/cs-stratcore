"""Scaffold integrity tests for doctrine-first repository shape."""

from importlib import import_module


def test_root_package_importable() -> None:
    module = import_module("cs_stratcore")
    assert hasattr(module, "__version__")
