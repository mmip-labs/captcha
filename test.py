from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random


custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-agent={custom_user_agent}')

widths = [1366, 1440, 1536, 1920]
heights = [768, 900, 960, 1080]
chrome_options.add_argument(f"--window-size={random.choice(widths)},{random.choice(heights)}")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.execute_cdp_cmd(
    'Emulation.setTimezoneOverride',
    {'timezoneId': 'America/New_York'}
)

driver.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "accuracy": 100
    }
)

driver.get('https://www.mobzystems.com/online/browser-information/')


time.sleep(5)


#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(40)

