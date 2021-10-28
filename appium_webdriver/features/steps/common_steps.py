from behave import *
import test_data


# Then I should see a message saying <message>
@then('I should see a message saying {message}')
def step_impl(context, message):
    element = test_data.driver.find_element_by_xpath("//*[@text='" + message + "']")
    assert element.is_displayed()
