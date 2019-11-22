import pytest
from lib import do_something
from pytest_testconfig import config
valore = config['something']['a_value']
def test_import():
    assert do_something() == valore
