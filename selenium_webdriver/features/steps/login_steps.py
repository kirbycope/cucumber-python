from behave import *
import selenium_webdriver.features.pages.login_page as login_page


# Given I am on the login page
@given('I am on the login page')
def step_impl(context):
    login_page.open()


# When I login with <username> and <password>
@when('I login with {username} and {password}')
def step_impl(context, username, password):
    login_page.login(username, password)
