from behave import *
import test_data


# I open the scene <name>
@given('I open the scene {name}')
def step_impl(context, name):
    # Loads the scene mentioned by its name.
    test_data.altUnityDriver.load_scene(name)
