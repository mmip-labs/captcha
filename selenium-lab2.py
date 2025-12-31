from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ya.ru')

time.sleep(10)

driver.back()

time.sleep(10)

driver.refresh()

time.sleep(10)
