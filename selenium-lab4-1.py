from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ylilit.ru/cart')

driver.find_element("id", "name").send_keys('H')
time.sleep(0.5)
driver.find_element("id", "name").send_keys('e')
time.sleep(0.5)
driver.find_element("id", "name").send_keys('l')
time.sleep(0.5)
driver.find_element("id", "name").send_keys('l')
time.sleep(0.5)
driver.find_element("id", "name").send_keys('o')

#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(5)

