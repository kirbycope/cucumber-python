import test_data


# MainActivity.kt


def editTextEnterAMessage():
    """ The `editText` with the placeholder 'Enter a messsage'. """
    return test_data.driver.find_element_by_id("editTextTextPersonName")


def buttonSend():
    """ The 'SEND' `button`. """
    return test_data.driver.find_element_by_id("button")

def open():
    """ Opens _this_ activity """
    print()

def send_message():
    print()