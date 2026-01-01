from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent
from func import random_lang, random_timezone

ua = UserAgent()
user_agent = ua.random

timezone = random_timezone()

print(user_agent)

chrome_options = webdriver.ChromeOptions()

# Set random user_agent
chrome_options.add_argument(f'--user-agent={user_agent}')

# Set language
language = random_lang()
chrome_options.add_argument(f'--lang={language}')
chrome_options.add_argument(f'--accept-lang={language}')

# Disable Features That Might Expose Automation
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

chrome_options.add_argument('--disable-blink-features=AutomationControlled')

chrome_options.add_argument("--headless=new")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set random screen size
widths = [1366, 1440, 1536]
heights = [768, 900, 960]
driver.set_window_size(random.choice(widths), random.choice(heights))

# --- Timezone ---
driver.execute_cdp_cmd(
    "Emulation.setTimezoneOverride",
    {"timezoneId": timezone}
)

# --- Убираем webdriver=true ---
driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});
""")


driver.get('https://www.mobzystems.com/online/browser-information/')

#driver.get('https://webbrowsertools.com/timezone/')


#driver.get('https://httpbin.org/user-agent')

print(driver.execute_script("return navigator.userAgent"))
print(driver.execute_script("return navigator.language"))
print(driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone"))
print(driver.execute_script("return window.innerWidth + 'x' + window.innerHeight"))


#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(30)

