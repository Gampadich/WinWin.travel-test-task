import pytest

@pytest.fixture(scope='session')
def url():
    return 'https://winwin.travel/'
