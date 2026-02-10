"""Tests for utility functions."""

from {{ cookiecutter.package_name }}.utils import hello_experiment


def test_hello_experiment() -> None:
    """Test that hello_experiment returns the expected greeting."""
    # Arrange & Act
    result = hello_experiment()

    # Assert
    assert isinstance(result, str)
    assert "Hello" in result
    assert "{{ cookiecutter.project_name }}" in result
