import time
from datetime import timedelta
from selenium import webdriver
import chromedriver_binary # required, do not remove
import test_data


def before_scenario(context, scenario):
    test_data.init()
    test_data.time_start = time.time()
    test_data.driver = webdriver.Chrome()
    test_data.driver.maximize_window()
    test_data.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    test_data.driver.quit()
    test_data.time_end = time.time()
    time_taken = str(timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')