"""Tests for package_name."""
import pytest

# from package_name import example_function


def test_example():
    """Example test case."""
    # Replace with actual tests
    assert True


def test_with_fixture(tmp_path):
    """Example test using pytest fixture."""
    # tmp_path is a built-in pytest fixture
    test_file = tmp_path / "test.txt"
    test_file.write_text("test content")
    assert test_file.read_text() == "test content"
