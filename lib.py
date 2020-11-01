from pytest_testconfig import config


def do_something():
    return config['something']['a_value']
