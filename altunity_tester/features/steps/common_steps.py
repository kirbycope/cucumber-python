from behave import *
import test_data


# I open the <name> scene
@given('I open the {name} scene')
def step_impl(context, name):
    # Loads the scene mentioned by its name.
    test_data.altUnityDriver.load_scene(name)
