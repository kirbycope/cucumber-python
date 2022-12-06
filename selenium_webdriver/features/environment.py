import time
from datetime import timedelta
from selenium import webdriver
import chromedriver_binary  # required, do not remove
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


def start_session():
    """ Starts a session with the global webdriver. """
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    test_data.driver = webdriver.Chrome(chrome_options=opts)
    test_data.driver.maximize_window()
    test_data.driver.implicitly_wait(5)
