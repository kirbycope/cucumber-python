from time import sleep
import test_data
from selenium.webdriver.common.by import By


# MainActivity.kt


def editTextEnterAMessage():
    """ The `editText` with the placeholder 'Enter a messsage'. """
    return test_data.driver.find_element(By.ID, "editTextTextPersonName")


def buttonSend():
    """ The 'SEND' `button`. """
    return test_data.driver.find_element(By.ID, "button")


def open():
    """ Opens _this_ activity. """
    print() # being the default activity there is nothing to do here


def send_message(message):
    """ Enters the given message and then clicks the 'SEND' button. """
    editTextEnterAMessage().send_keys(message)
    buttonSend().click()
    sleep(.250)
