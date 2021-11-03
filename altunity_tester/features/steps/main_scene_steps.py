from behave import *
import altunity_tester.features.scenes.main_scene as main_scene


# Given I am on the main scene
@given('I am on the main scene')
def step_impl(context):
    main_scene.open()
