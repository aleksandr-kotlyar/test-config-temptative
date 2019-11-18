import pytest
from pytest_testconfig import config

def test_something():
    assert config['something']['a_value'] == "the value"