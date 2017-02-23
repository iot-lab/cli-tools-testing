import pytest


@pytest.fixture(scope="module")
def exp():
    """ a popo for storing experiment id across tests """
    class _exp: id = None
    return _exp()
