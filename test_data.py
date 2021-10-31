import os
from dotenv import load_dotenv, find_dotenv

def init():
    global server; server = None
    global driver; driver = None
    global time_start; time_start = None
    global time_end; time_end = None
    load_dotenv(find_dotenv())
    global base_url; base_url = os.environ.get("TEST_BASE_URL")
    global test_user; test_user = os.environ.get("TEST_USER")
    global test_pass; test_pass = os.environ.get("TEST_PASS")