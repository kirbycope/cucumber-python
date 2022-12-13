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
    print("Forwarding port for AltUnity...")
    if "headspin" in test_data.hub_uri:
        connect_headspin()
    elif "saucelabs" in test_data.hub_uri:
        connect_saucelabs()
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
    print("Starting Appium Server...")
    test_data.server = AppiumService()
    pwd = sys.path[0]
    script = pwd + "/node_modules/appium/build/lib/main.js"
    test_data.server.start(main_script=script, args=['--base-path', '/wd/hub'])
    print("Started.")


def start_session():
    """ Starts a session with the global webdriver. """
    platform_name = from_config("PLATFORMNAME")
    udid = from_config("UDID")
    caps = {
        "appium:udid": udid,
        "platformName": platform_name,
        "newCommandTimeout": 999
    }
    if "headspin" in test_data.hub_uri:
        caps["autoGrantPermissions"] = True
        caps["headspin:appId"] = from_config("APPID")
        caps["headspin:capture"] = True
        caps["headspin:controlLock"] = True
        caps["headspin:newcommandtimeout"] = 120
        token = from_env("HEADSPIN_TOKEN")
        hub_uri = test_data.hub_uri + "/" + token + "/wd/hub"
    elif "saucelabs" in test_data.hub_uri:
        caps["appium:app"] = "storage:filename=" + from_config("APPID")
        caps['appium:automationName'] = 'UiAutomator2'
        caps['sauce:options'] = {}
        caps['sauce:options']['build'] = '<your build id>'
        caps['sauce:options']['name'] = '<your test name>'
        username = from_env("SAUCE_USERNAME")
        access_key = from_env("SAUCE_ACCESS_KEY")
        hub_uri = f"https://{username}:{access_key}@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    else:
        app = os.path.join(sys.path[0], "altunity_tester", from_config("APP"))
        caps["appium:app"] = app
        hub_uri = test_data.hub_uri
    print("Starting Appium WebDriver...")
    test_data.driver = webdriver.Remote(command_executor=hub_uri, desired_capabilities=caps)
    test_data.driver.implicitly_wait(30)
    print("Session ID: " + test_data.driver.session_id)


def stop_debug_timer():
    """ Prints diff of `test_data.time_start` and `test_data.time_end`. """
    test_data.time_end = time.time()
    time_taken = str(
        timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')


def connect_headspin():
    devices = headspin.devices()
    udid = from_config("UDID")
    host_name = headspin.device_hostname(devices, udid)
    os.system("hs connect -t {} {}@{}".format(test_data.headspin_token, udid, host_name))


def connect_saucelabs():
    sauce_jar = from_env("SAUCE_VUSB_JAR")
    start_vusb = f"java -jar {sauce_jar} server --datacenter US"
    os.popen(start_vusb)
    username = from_env("SAUCE_USERNAME")
    access_key = from_env("SAUCE_ACCESS_KEY")
    get_sessions = f"java -jar {sauce_jar} sessions --username {username} --accessKey {access_key}"
    sessions = os.popen(get_sessions).read()
    sauce_session_id = sessions.split("\n")[2].split()[0]
    connect_session = f"java -jar {sauce_jar} connect --sessionId {sauce_session_id} --username {username} --accessKey {access_key}"
    os.system(connect_session)
    try:
        os.system("adb connect localhost:7000")
    except:
        os.system("adb connect localhost:7001")
