from behave import *
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from setuptools import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('I launch Chrome browser')
def step_impl(context):
    service = Service(executable_path=ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

@when('I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}" and email "{email}"')
def step_impl(context, user, pwd, email):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, "btnLogin").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    dashboard_element = context.driver.find_element(By.CLASS_NAME, "oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module")
    bool_displayed = dashboard_element.isDisplayed()

    assert bool_displayed == True