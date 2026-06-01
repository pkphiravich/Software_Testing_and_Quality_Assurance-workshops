import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():

	service = ChromeService(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	driver.get("https://www.testmu.ai/selenium-playground/")
	# driver.implicit_wait(5)
	yield driver
	driver.quit()


def test_one(driver):
	simple_form_demo = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/section[2]/div/ul/li[34]/a')
	simple_form_demo.click()
	time.sleep(3)

	input_text = driver.find_element(By.XPATH, '//*[@id="user-message"]')
	input_text.send_keys("PK")
	time.sleep(3)

	submit = driver.find_element(By.XPATH, '//*[@id="showInput"]')
	submit.click()
	time.sleep(3)

	show_text = driver.find_element(By.XPATH, '//*[@id="message"]')
	assert show_text.text == "PK"






def test_two(driver):
	checkbox_demo = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/section[2]/div/ul/li[9]/a')
	checkbox_demo.click()
	time.sleep(3)

	i = 1
	while i < 5:
		option = driver.find_element(By.NAME, f"option{i}")
		is_selected = option.is_selected()
		assert not is_selected
		i = i+ 1
	
	check_all = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/section/div/div/div[3]/button')
	check_all.click()
	time.sleep(3)

	i = 1
	while i < 5:
		option = driver.find_element(By.NAME, f"option{i}")
		is_selected = option.is_selected()
		assert is_selected
		i = i+ 1



def test_three(driver):
	drop_down = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/section[2]/div/ul/li[32]/a')
	drop_down.click()
	time.sleep(3)

	select_ = driver.find_element(By.XPATH, '//*[@id="select-demo"]')
	select_.send_keys("Friday")
	time.sleep(5)

	day_selected = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div/div/div/div[1]/div[2]/p')
	assert day_selected.text == 'Day selected :- Friday'



def test_four(driver):
	bootsteap_ = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div/ul/li[7]/a')
	bootsteap_.click()
	time.sleep(3)

	download = driver.find_element(By.XPATH, '//*[@id="dwnBtn"]')
	download.click()
	time.sleep(3)

	bar = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div/div/div/div/div/div/div/p')
	assert bar.text == '100%'
	time.sleep(3)

	progress = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/section[2]/div/div/div/div/div/div/p')
	assert progress.text == 'Download completed!'


















# def test_five(driver):
# 	pass