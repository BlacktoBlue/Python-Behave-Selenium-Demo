from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given("I open a browser")
def step_impl(context):
    driver = webdriver.Chrome()
    context.driver = driver

@step("I navigate to {url}")
def step_impl(context, url):
    context.driver.get(f"http://{url}")


@when('I enter "{search_term}" in the search field')
def step_impl(context, search_term):
    elem = context.driver.find_element(By.NAME, "q")
    context.driver.find_element(By.ID, "L2AGLb").click()

    elem.clear()
    elem.send_keys(search_term)


@when("I click search")
def step_impl(context):
    elem = context.driver.find_element(By.NAME, "btnK")
    elem.click()


@then("I see the results")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I see the results')

