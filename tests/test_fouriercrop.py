"""Tests for `fouriercrop` module."""

from typing import Generator

import pytest

import fouriercrop


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield fouriercrop.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == fouriercrop.__version__
