"""
This contains shared fixtures.

"""
# Importing required Libraries
import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    # Read the json file
    with open('./../config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0

    # return config to be used
    return config

@pytest.fixture
def driver(config):
    #Initialize webdriver instance
    if config['browser']=='Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser']=='Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported.')

    #Wait till it gets opened
    b.implicitly_wait(config['implicit_wait'])
    b.maximize_window()

    # Returning webdriver instance for the setup
    yield b

    # Quitting webdriver instance for the cleanup
    b.quit()
