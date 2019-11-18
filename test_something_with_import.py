import pytest
from lib import do_something
from pytest_testconfig import config
def test_import():
    assert do_something() == "the value"
