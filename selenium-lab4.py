from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://mail.mmip.ru')

driver.find_element("id", "rcmloginuser").send_keys('Hello')

driver.find_element("id", "rcmloginsubmit").click()

time.sleep(5)

