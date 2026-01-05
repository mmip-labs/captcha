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
    '2': '178.208.91.155:8888',
    '3': '193.33.184.68:8000'
}

def run_task(proxy, language, timezone):

    ua = UserAgent()
    user_agent = ua.random

    #timezone = random_timezone()

    chrome_options = webdriver.ChromeOptions()

    # Set language
    chrome_options.add_argument(f'--lang={language}')
    chrome_options.add_argument(f'--accept-lang={language}')

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


    # Set time zone
    driver.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone}
    )

    # Unset webdriver=true
    driver.execute_script("""
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """)

    # Maximize windows
    driver.maximize_window()

    # Get pages
    driver.get('https://ylilit.ru/cart')

    timers = [0.2, 0.3]

    dishes = make_menu()


    dish_id = random.choice(list(dishes.keys()))
    dish_name = dishes[dish_id][0]
    dish_value = dishes[dish_id][1]
    dish_img = dishes[dish_id][2]
    dish_price = dishes[dish_id][3]

    dish_img = 'https://tn.fishki.net/26/upload/post/2026/01/03/4976784/bd3a55911643da8f200c92cf2f78aa45.jpg'

    print(dish_id, dish_name, dish_value, dish_price)
    print()

    driver.execute_script("window.cart['1112'] = '[]';")

    driver.execute_script(f'window.cart["1112"] = [1,"{dish_img}","{dish_value}","{dish_name}","{dish_price}"];')

    # Sleep before filling fields
    time.sleep(random.choice([3, 8]))

    # Phone number
    driver.find_element(By.ID, "tel").click()
    time.sleep(2)
    for digit in get_phone_number():
        driver.find_element(By.ID, "tel").send_keys(f'{digit}')
        timeout = random.choice(timers)
        time.sleep(timeout)

    time.sleep(random.choice([2, 3, 4, 5]))
    # Name
    driver.find_element(By.ID, "name").click()
    time.sleep(1.5)
    for char in get_name():
        driver.find_element(By.ID, "name").send_keys(f'{char}')
        timeout = random.choice(timers)
        time.sleep(timeout)

    time.sleep(random.choice([2, 3, 4, 5]))

    # Email
    driver.find_element(By.ID, "mail").click()
    time.sleep(1.5)
    for email in get_email():
        driver.find_element(By.ID, "mail").send_keys(f'{email}')
        timeout = random.choice(timers)
        time.sleep(timeout)

    time.sleep(random.choice([2, 3, 4, 5]))

    # Address
    driver.find_element(By.ID, "adress").click()
    time.sleep(2)
    for address in get_random_yaroslavl_address():
        driver.find_element(By.ID, "adress").send_keys(f'{address}')
        time.sleep(0.5)

    time.sleep(random.choice([2, 3, 4, 5]))

    # Form submit
    driver.find_element(By.CLASS_NAME, "sendCart").click()

    time.sleep(600)
    driver.close()

last_proxy = 3

proxy = proxies[str(last_proxy)]
lang = 'nl-NL,nl;q=0.9,en-US;q=0.8'
tz = 'Europe/Amsterdam'


print(f'{datetime.now()}, Proxy: {proxy}, ID: {last_proxy}, Lang: {lang}, TZ: {tz}')
run_task(proxy=proxy, language=lang, timezone=tz)


