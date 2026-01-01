from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent


ua = UserAgent()
user_agent = ua.random

print(user_agent)

chrome_options = webdriver.ChromeOptions()

# Set random user_agent
chrome_options.add_argument(f'--user-agent={user_agent}')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set random screen size
widths = [1366, 1440, 1536]
heights = [768, 900, 960]
driver.set_window_size(random.choice(widths), random.choice(heights))

# driver.execute_cdp_cmd(
#     "Emulation.setTimezoneOverride",
#     {"timezoneId": "America/New_York"}
# )

driver.get('https://www.mobzystems.com/online/browser-information/')
#driver.get('https://httpbin.org/user-agent')



#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(30)

