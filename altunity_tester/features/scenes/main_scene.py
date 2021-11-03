import test_data
from altunityrunner import *

# Main scene


def btnClose():
    """ The "close" `button`. """
    return test_data.altUnityDriver.find_object(By.NAME, "Close Button")


def btnFoo():
    """ Some `button`. """
    return test_data.altUnityDriver.find_object(By.NAME, "Button")


def open():
    """ Opens _this_ scene. """
    print() # being the default scene there is nothing to do here


def open_close_panel():
    btnClose().tap()
    btnFoo.tap()
