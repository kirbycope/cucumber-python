from behave import *
import appium_webdriver.features.activities.main_activity as main_activity


# Given I am on the main activity
@given('I am on the main activity')
def step_impl(context):
    main_activity.open()


# When I send a message saying <message>
@when('I send a message saying {message}')
def step_impl(context, message):
    main_activity.send_message(message)
