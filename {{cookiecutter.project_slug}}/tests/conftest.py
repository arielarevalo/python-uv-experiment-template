"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_data() -> list[int]:
    """Provide sample data for tests.

    Returns:
        A list of sample integers.
    """
    return [1, 2, 3, 4, 5]
