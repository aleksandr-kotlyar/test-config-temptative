import pytest
from pytest_testconfig import config

from lib import do_something


def test_something():
    assert config['something']['a_value'] == "the value"


def test_something2():
    assert do_something() == "the value"
