import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
pref = {
        "profile.password_manager_leak_detection": False
    }
chrome_options.add_experimental_option("prefs", pref)


# ก่อนเริ่มให้สร้าง web driver ขึ้นมา เก็บไว้ใน context; dictionary
def before_scenario(context,scenario):
    context.driver = webdriver.Chrome(options=chrome_options)

def after_scenario(context,scenario):
    context.driver.quit() # close scenario; test case

def after_step(context, step):
    time.sleep(2)


