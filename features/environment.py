import time
from datetime import timedelta
import test_data as testdata


def before_scenario(context, Scenario):
    testdata.init()
    testdata.time_start = time.time()


def after_scenario(context, scenario):
    testdata.time_end = time.time()
    time_taken = str(timedelta(seconds=testdata.time_end - testdata.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')
