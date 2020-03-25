import pytest
from pytest_testconfig import config
value = config['something']['a_value']

@pytest.fixture()
def fixture_me():
    return value


