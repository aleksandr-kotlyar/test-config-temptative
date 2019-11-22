from pytest_testconfig import config

valore = config['something']['a_value']

def do_something():
    return valore