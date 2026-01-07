from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
import string
from func import get_phone_number, get_name, get_email, get_random_yaroslavl_address, make_menu
#from func import random_timezone
from fake_useragent import UserAgent
from datetime import datetime

proxies = {
    '1': '178.208.91.155:8888',
    '2': '72.56.79.240:8888',
    '3': '193.33.184.68:8000'
}

def run_task(proxy):

    ua = UserAgent()
    user_agent = ua.random

    #timezone = random_timezone()

    chrome_options = webdriver.ChromeOptions()

    # Set language
    #chrome_options.add_argument(f'--lang={language}')
    #chrome_options.add_argument(f'--accept-lang={language}')

    # Set window size
    widths = [1366, 1440, 1536]
    heights = [768, 900, 960]

    chrome_options.add_argument(f"--window-size={random.choice(widths)},{random.choice(heights)}")

    # Disable Features That Might Expose Automation
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Proxy
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")


    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Headless mode
    #chrome_options.add_argument("--headless=new")


    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)




    # Unset webdriver=true
    driver.execute_script("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """)

    # Maximize windows
    driver.maximize_window()

    # Get pages
    driver.get('https://t.mmip.ru')


    time.sleep(500)
    driver.close()

last_proxy = 2

proxy = proxies[str(last_proxy)]
#lang = 'nl-NL,nl;q=0.9,en-US;q=0.8'
#tz = 'Europe/Amsterdam'


print(f'{datetime.now()}, Proxy: {proxy}, ID: {last_proxy}')
run_task(proxy=proxy)


