from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://mail.mmip.ru')

url = driver.current_url

print(url)



#assert url == 'https://mail.mmip.ru/webmail/', 'Error'

print(driver.page_source)


time.sleep(5)