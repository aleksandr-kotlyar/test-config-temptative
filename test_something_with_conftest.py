import pytest
from pytest_testconfig import config

def test_using_fixture(fixture_me):
    print(fixture_me)