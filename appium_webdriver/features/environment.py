from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from datetime import timedelta
from helpers.config import from_config, from_env
import os
import time
import configparser
import test_data
import sys


def before_all(context):
    """ This runs before after the whole shooting match. """
    test_data.init()
    test_data.time_start = time.time()
    start_server()


def after_all(context):
    """ This runs before after the whole shooting match. """
    test_data.server.stop()
    stop_debug_timer()


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    start_session()


def after_scenario(context, scenario):
    """ This runs after each scenario. """
    test_data.driver.quit()


def read_from_config(key):
    """ Read the value of the given key from the configuration file. """
    config = configparser.ConfigParser()
    config.read("appium.ini")
    return config["DEFAULT"][key]


def start_server():
    test_data.server = AppiumService()
    pwd = sys.path[0]
    script = pwd + "/node_modules/appium/build/lib/main.js"
    test_data.server.start(main_script=script, args=['--base-path', '/wd/hub'])


def start_session():
    """ Starts a session with the global webdriver. """
    app = os.path.join(sys.path[0], "appium_webdriver", read_from_config("APP"))
    desired_capabilities = {
        "appium:app": app,
        "appium:udid": read_from_config("UDID"),
        "platformName": read_from_config("PLATFORMNAME")
    }
    command_executor = read_from_config("HUBURI")
    test_data.driver = webdriver.Remote(command_executor, desired_capabilities)
    test_data.driver.implicitly_wait(5)


def stop_debug_timer():
    """ Prints diff of `test_data.time_start` and `test_data.time_end`. """
    test_data.time_end = time.time()
    time_taken = str(timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')
