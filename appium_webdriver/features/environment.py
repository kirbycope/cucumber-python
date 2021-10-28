from appium import webdriver
from datetime import timedelta
import time
import configparser
import test_data


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    test_data.init()
    test_data.time_start = time.time()
    start_session()


def after_scenario(context, scenario):
    """ This runs after each scenario. """
    test_data.driver.quit()
    test_data.time_end = time.time()
    time_taken = str(timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')


def read_from_config(key):
    """ Read the value of the given key from the configuration file. """
    config = configparser.ConfigParser()
    config.read("appium.ini")
    return config["DEFAULT"][key]


def start_session():
    """ Starts a session with the global webdriver. """
    desired_capabilities = {
        "appium:app": read_from_config("APP"),
        "appium:udid": read_from_config("UDID"),
        "platformName": read_from_config("PLATFORMNAME")
    }
    command_executor = read_from_config("HUBURI")
    test_data.driver = webdriver.Remote(command_executor, desired_capabilities)
    test_data.driver.implicitly_wait(5)
