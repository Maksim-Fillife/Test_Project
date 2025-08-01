import pytest

@pytest.fixture
def before_after_test():
    print("Before test")
    yield
    print("\nAfter test")

def test_api_1():
    assert 2 + 2 == 4

def test_api_2(before_after_test):
    assert 2 + 3 == 5
