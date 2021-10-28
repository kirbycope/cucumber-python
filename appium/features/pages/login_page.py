import test_data


# URL looks like: {baseURL}/login


def inputUserName():
    """ The `input` for "Username". """
    return test_data.driver.find_element_by_id('username')


def inputPassword():
    """ The `input` for "Password". """
    return test_data.driver.find_element_by_id('password')


def btnSubmit():
    """ The `button` to submit a form. """
    return test_data.driver.find_element_by_css_selector('button[type="submit"]')


def open():
    """ Opens `this` page. """
    test_data.driver.get(test_data.base_url + '/login')


def login(username, password):
    """ Log in using the given username and password. """
    if username == 'valid':
        username = test_data.test_user
    if password == 'valid':
        password = test_data.test_pass
    inputUserName().send_keys(username)
    inputPassword().send_keys(password)
    btnSubmit().click()
