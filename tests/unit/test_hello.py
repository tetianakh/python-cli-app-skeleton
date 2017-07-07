import pytest

import myapp


@pytest.fixture
def hello():
    return 'hello'


def test_hello(hello):
    assert hello == 'hello'
