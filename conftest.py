import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")

def browser():
	chrome_path = "/home/lucasrm/dash/chrome-linux64/chrome"  # Substitua pelo caminho correto do seu Chrome
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = chrome_path
	driver = webdriver.Chrome(options=chrome_options)
	yield driver
	driver.quit()
