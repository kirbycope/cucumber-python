import os
from dotenv import load_dotenv, find_dotenv

def init():
    global server; server = None
    global driver; driver = None
    global hub_uri; hub_uri = None
    global altUnityDriver; altUnityDriver = None
    global time_start; time_start = None
    global time_end; time_end = None
    load_dotenv(find_dotenv())
    global base_url; base_url = os.environ.get("TEST_BASE_URL")
    global test_user; test_user = os.environ.get("TEST_USER")
    global test_pass; test_pass = os.environ.get("TEST_PASS")
    global headspin_token; headspin_token = os.environ.get("HEADSPIN_TOKEN")
    global sauce_jar; sauce_jar = os.environ.get("SAUCE_VUSB_JAR")
