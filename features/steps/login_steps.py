from behave import *

# Given I am on the login page
@given('I am on the login page')
def step_impl(context):
    # LoginPage.open()
    pass

# When I login with <username> and <password>
@given('I enter {message}')
def step_impl(context, message):
    print()
