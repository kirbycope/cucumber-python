from behave import *
import test_data
from selenium.webdriver.common.by import By

# Then I should see a message saying <message>
@then('I should see a message saying {message}')
def step_impl(context, message):
    element = test_data.driver.find_element(By.XPATH"//*[@text='" + message + "']")
    assert element.is_displayed()
