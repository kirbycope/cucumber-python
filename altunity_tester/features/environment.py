from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from altunityrunner import *
from datetime import timedelta
from helpers.config import from_config, from_env
import time
import os
import test_data
import sys
import headspin


def before_all(context):
    """ This runs before the whole shooting match. """
    test_data.init()
    test_data.time_start = time.time()
    test_data.hub_uri = from_config("HUBURI")
    if "local" in test_data.hub_uri:
        start_server()


def after_all(context):
    """ This runs after the whole shooting match. """
    if "local" in test_data.hub_uri:
        test_data.server.stop()
    stop_debug_timer()


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    start_session()
    print("Forwaring port for AltUnity...")
    if "headspin" in test_data.hub_uri:
        devices = headspin.devices()
        udid = from_config("UDID")
        host_name = headspin.device_hostname(devices, udid)
        os.system("hs connect -t {} {}@{}".format(test_data.headspin_token, udid, host_name))
    AltUnityPortForwarding.forward_android()
    test_data.altUnityDriver = AltUnityDriver()
    print("Forwarded.")


def after_scenario(context, scenario):
    """ This runs after each scenario. """
    test_data.driver.quit()
    test_data.altUnityDriver.stop()
    if "local" in test_data.hub_uri:
        AltUnityPortForwarding.remove_forward_android()


def start_server():
    print("String Appium Server...")
    test_data.server = AppiumService()
    pwd = sys.path[0]
    script = pwd + "\\node_modules\\appium\\build\\lib\\main.js"
    test_data.server.start(main_script=script)
    print("Started.")


def start_session():
    """ Starts a session with the global webdriver. """
    platform_name = from_config("PLATFORMNAME")
    udid = from_config("UDID")
    caps = {
        "appium:udid": udid,
        "platformName": platform_name
    }
    if "headspin" in test_data.hub_uri:
        caps["autoGrantPermissions"] = True
        caps["headspin:appId"] = from_config("APPID")
        caps["headspin:capture"] = True
        caps["headspin:controlLock"] = True
        caps["headspin:newcommandtimeout"] = 120
        token = from_env("HEADSPIN_TOKEN")
        hub_uri = test_data.hub_uri + "/" + token + "/wd/hub"
    else:
        caps["appium:app"] = from_config("APP")
        hub_uri = test_data.hub_uri
    print("Starting Appium WebDriver...")
    test_data.driver = webdriver.Remote(command_executor=hub_uri, desired_capabilities=caps)
    test_data.driver.implicitly_wait(5)
    print("Session ID: " + test_data.driver.session_id)


def stop_debug_timer():
    """ Prints diff of `test_data.time_start` and `test_data.time_end`. """
    test_data.time_end = time.time()
    time_taken = str(
        timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')
