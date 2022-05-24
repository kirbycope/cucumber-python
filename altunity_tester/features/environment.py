from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from altunityrunner import *
from datetime import timedelta
import time
import configparser
import os
import test_data
import sys
import headspin

def before_all(context):
    """ This runs before after the whole shooting match. """
    test_data.init()
    test_data.time_start = time.time()
    test_data.hub_uri = read_from_config("HUBURI")
    if "local" in test_data.hub_uri:
        start_server()


def after_all(context):
    """ This runs before after the whole shooting match. """
    test_data.server.stop()
    stop_debug_timer()


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    start_session()
    if "headspin" in test_data.hub_uri:
        devices = headspin.devices()
        udid = read_from_config("UDID")
        host_name = headspin.device_hostname(devices, udid)
        os.system("hs connect -t {} {}@{}".format(test_data.token, udid, host_name))
    AltUnityPortForwarding.forward_android()
    test_data.altUnityDriver = AltUnityDriver()


def after_scenario(context, scenario):
    """ This runs after each scenario. """
    test_data.driver.quit()
    test_data.altUnityDriver.stop()
    if "local" in test_data.hub_uri:
        AltUnityPortForwarding.remove_forward_android()


def read_from_config(key):
    """ Read the value of the given key from the configuration file. """
    config = configparser.ConfigParser()
    config.read("altunity.ini")
    return config["DEFAULT"][key]


def start_server():
    test_data.server = AppiumService()
    pwd = sys.path[0]
    script = pwd + "\\node_modules\\appium\\build\\lib\\main.js"
    test_data.server.start(main_script=script)


def start_session():
    """ Starts a session with the global webdriver. """
    desired_capabilities = {
        "appium:udid": read_from_config("UDID"),
        "platformName": read_from_config("PLATFORMNAME")
    }
    if "headspin" in test_data.hub_uri:
        desired_capabilities["autoGrantPermissions"] = True
        desired_capabilities["headspin:appId"] = read_from_config("APPID")
        desired_capabilities["headspin:capture"] = True
        desired_capabilities["headspin:controlLock"] = True
        desired_capabilities["headspin:newcommandtimeout"] = 120
        desired_capabilities["headspin:waitForDeviceOnlineTimeout"] = 120
        command_executor = test_data.hub_uri + "/" + test_data.token + "/wd/hub"
    else:
        desired_capabilities["appium:app": read_from_config("APP")]
        command_executor = test_data.hub_uri
    test_data.driver = webdriver.Remote(command_executor, desired_capabilities)
    test_data.driver.implicitly_wait(5)


def stop_debug_timer():
    """ Prints diff of `test_data.time_start` and `test_data.time_end`. """
    test_data.time_end = time.time()
    time_taken = str(
        timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')
