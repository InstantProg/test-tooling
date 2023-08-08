from behave import *
from selenium import webdriver


@given("I have entered 50 and 70 into the calculator")
def step_impl(context):
    values_entered = calculator(50, 70)

@when("I press add")
def step_impl(context):
    print(calculator(50, 70))

@then("the result should be 120 on screen")
def step_impl(context):
    result = calculator(50, 70)
    assert  result == 120


def calculator(x, y):
    return x + y