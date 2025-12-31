from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

time.sleep(5)
