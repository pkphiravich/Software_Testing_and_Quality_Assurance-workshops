from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException
from behave import *


@given(u'ฉันเข้าไปที่หน้าเว็บหลักของ Swag Lab')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")


@then(u'ฉันจะเห็นว่าในหน้าเว็บมี title ที่เขียนว่า "swag labs"')
def step_impl(context):
    title = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]')
    assert title.text.lower() == 'swag labs' 


@when(u'ฉันใส่ login ว่า "{username}"')
def step_impl(context ,username):
    log = context.driver.find_element(By.ID, 'user-name')
    log.send_keys(username)


@when(u'ฉันใส่ password ว่า "{password}"')
def step_impl(context, password):
    pass_ = context.driver.find_element(By.ID, 'password')
    pass_.send_keys(password)


@when(u'ฉันกดปุ่ม Login')
def step_impl(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then(u'ฉันต้องเห็นคำว่า "Products" ขึ้นในหน้าเว็บ')
def step_impl(context):
    products = context.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    assert products.text.lower() == 'products'


@then(u'ระบบต้องแจ้งเตือนมาว่า "Username and password do not match any user in this service"')
def step_impl(context):
    warn = context.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert warn.text == "Epic sadface: Username and password do not match any user in this service"


@when(u'ฉันกดปุ่ม ADD TO CART สักปุ่มบนหน้าจอ')
def step_impl(context):
    add_item = context.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_item.click()


@then(u'icon รูปบนตะกร้าต้องมีเลข 1 ขึ้นมา')
def step_impl(context):
    num = context.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert num.text == "1"


@when(u'ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Backpack')
def step_impl(context):
    add_item = context.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_item.click()


@when(u'ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Bike Light')
def step_impl(context):
    add_item = context.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    add_item.click()


@when(u'ฉันกดปุ่ม ADD TO CART ของสินค้า Sauce Labs Bolt T-Shirt')
def step_impl(context):
    add_item = context.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    add_item.click()


@then(u'icon รูปบนตะกร้าต้องมีเลข 3 ขึ้นมา')
def step_impl(context):
    num = context.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert num.text == "3"


@then(u'ฉันกดปุ่ม icon รูปตะกร้า')
def step_impl(context):
    icon = context.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    icon.click()


@then(u'ฉันกดปุ่ม checkout')
def step_impl(context):
    checkout = context.driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()


@then(u'ฉันกรอก first name ว่า "{first_name}"')
def step_impl(context ,first_name):
    fname = context.driver.find_element(By.ID, 'first-name')
    fname.send_keys(first_name)


@then(u'ฉันกรอก last name ว่า "{last_name}"')
def step_impl(context ,last_name):
    lname = context.driver.find_element(By.ID, 'last-name')
    lname.send_keys(last_name)


@then(u'ฉันกรอก postal code ว่า "{postal_code}"')
def step_impl(context ,postal_code):
    pcode = context.driver.find_element(By.ID, 'postal-code')
    pcode.send_keys(postal_code)


@then(u'ฉันกดปุ่ม continue')
def step_impl(context):
    continue_ = context.driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_.click()
    

@then(u'ฉันเห็น "Item total: $55.97" ขึ้นในหน้าเว็บ')
def step_impl(context):
    item = context.driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    assert item.text == "Item total: $55.97"