"""This module contains all configurations for to ensure the correct execution of test cases."""

import json

import pytest
from selenium import webdriver


CONFIG_PATH = 'config.json'
CHROME_DRIVER_WIN_PATH = 'drivers/chromedriver_win.exe'
FIREFOX_DRIVER_PATH = 'drivers/geckodriver_win.exe'
DEFAULT_WAIT_TIME = 10
SUPPORTED_OPERATING_SYSTEMS = ['macOS', 'Windows']
SUPPORTED_BROWSERS = ['chrome', 'safari', 'firefox']

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)

    return data

@pytest.fixture(scope='session')
def config_operating_system(config):
    if 'operating_system' not in config:
        raise Exception('The config file does not contain the "os" key.')
    elif config['operating_system'] not in SUPPORTED_OPERATING_SYSTEMS:
        raise Exception('{operating_system} is not a supported operating system.'.format(operating_system=config['operating_system']))

    return config['operating_system']


@pytest.fixture(scope='session')
def config_wait_time(config):
    if 'wait_time' not in config:
        return DEFAULT_WAIT_TIME
    else:
        return config['wait_time']

@pytest.fixture(scope='function')
def driver(config_operating_system, browser, config_wait_time):
    if config_operating_system == 'macOS':
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'safari':
            driver = webdriver.Safari()
        else:
            raise Exception('{browser} is not a supported browser.'.format(browser=browser))
    elif config_operating_system == 'Windows':
        if browser == 'chrome':
            driver = webdriver.Chrome(executable_path=CHROME_DRIVER_WIN_PATH)
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=FIREFOX_DRIVER_PATH)
        else:
            raise Exception('{browser} is not a supported browser.'.format(browser=browser))
    else:
        raise Exception('{operating_system} is not a supported operating system.'.format(operating_system=config_operating_system))

    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    yield driver

    driver.quit()