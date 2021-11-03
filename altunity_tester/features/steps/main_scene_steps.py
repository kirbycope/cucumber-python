from behave import *
import test_data
from altunityrunner import *
import altunity_tester.features.scenes.main_scene as main_scene


# I start running and pause
@when('I start running and pause')
def step_impl(context):
    main_scene.start_run_then_pause()


# Then I should see the Pause Menu
@then('I should see the Pause Menu')
def step_impl(context):
    panelElement = test_data.altUnityDriver.wait_for_object(By.NAME, "Exit")
    assert panelElement.enabled
