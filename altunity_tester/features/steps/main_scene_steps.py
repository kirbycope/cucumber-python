from behave import *
import test_data
from altunityrunner import *
import altunity_tester.features.scenes.main_scene as main_scene


# When I foo
@when('I foo')
def step_impl(context):
    main_scene.open_close_panel()


# Then I bar
@then('I bar')
def step_impl(context):
    panelElement = test_data.altUnityDriver.wait_for_object(By.NAME, "Panel")
    test_data.assertTrue(panelElement.enabled)
