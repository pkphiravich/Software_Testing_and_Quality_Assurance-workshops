import time
from selenium import webdriver

# ก่อนเริ่มให้สร้าง web driver ขึ้นมา เก็บไว้ใน context; dictionary
def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context,scenario):
    context.driver.quit() # close scenario; test case

def after_step(context, step):
    time.sleep(2)