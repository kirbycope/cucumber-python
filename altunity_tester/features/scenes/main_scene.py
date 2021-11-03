import test_data
from altunityrunner import *

# "Main" scene


def btnRun():
    """ The "Run!" `button`. """
    return test_data.altUnityDriver.find_object(By.NAME, "StartButton")


def btnPause():
    """ The "||" (Pause) `button`. """
    return test_data.altUnityDriver.find_object(By.NAME, "pauseButton")


def open():
    """ Opens _this_ scene. """
    test_data.altUnityDriver.load_scene("Main")


def start_run_then_pause():
    """ Starts a run and then pauses after 10 seconds. """
    time.sleep(2)
    btnRun().tap()
    time.sleep(10)
    btnPause().tap()
