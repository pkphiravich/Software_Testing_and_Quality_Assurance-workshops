from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException
from behave import *

@given(u'ฉันเข้าไปที่หน้าเว็บ form ของ selenium')
def step_impl(context):
    context.driver.get("https://www.selenium.dev/selenium/web/web-form.html")


@then(u'ฉันจะเห็นว่าหน้าเว็บมี heading ที่เขียนว่า web form')
def step_impl(context):
    heading = context.driver.find_element(By.CSS_SELECTOR, 'h1')
    assert heading.text.lower() == "web form"


@when(u'ฉันใส่คำว่า "{textinput}" ลงใน text input')
def step_impl(context, textinput):
    context.driver.find_element(By.ID, 'my-text-id').send_keys(textinput) # to be all the more dynamically


@when(u'ฉันกดปุ่ม submit')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/button')


@then(u'ฉันควรจะเห็น message ขึ้นว่า "Received!"')
def step_impl(context):
    output = context.driver.find_element(By.ID, 'message')
    assert output.text.lower() == "Received!"
