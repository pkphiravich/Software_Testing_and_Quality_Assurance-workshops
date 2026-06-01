from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)
title = driver.title
assert title == "Web form"

try:
	heading = driver.find_element(By.CSS_SELECTOR,'h1')
	assert heading.text == "Web form"
except NoSuchElementException:
	assert False,"The element doesn't exist"

#----something more under here ------

# text_input = driver.find_element(By.ID, 'my-text-id')
text_input = driver.find_element(By.XPATH, '//*[@id="my-text-id"]')
text_input.send_keys("CS364")

# Click radio button

radio_button = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/div[2]/label')
radio_button.click()

submitB = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/button')
submitB.click()
time.sleep(5)


mytext = driver.find_element(By.XPATH, '//*[@id="message"]')
assert mytext.text == "Received!"
time.sleep(5)

#------------------------------------

#end the code with
driver.quit()