from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent
from func import random_lang, random_timezone
from datetime import datetime



proxies = {
    '1': '72.56.79.240:8888',
    '2': '178.208.91.155:8888',
    '3': '193.33.184.68:8000'
}
def run_task(proxy, language, timezone):
    ua = UserAgent()
    user_agent = ua.random

    #timezone = random_timezone()

    chrome_options = webdriver.ChromeOptions()

    # Set random user_agent
    chrome_options.add_argument(f'--user-agent={user_agent}')

    # Set language
    #language = random_lang()
    chrome_options.add_argument(f'--lang={language}')
    chrome_options.add_argument(f'--accept-lang={language}')

    # Disable Features That Might Expose Automation
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')

    # Proxy
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    #chrome_options.add_argument("--headless=new")

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

    driver.maximize_window()
    driver.get('https://www.mobzystems.com/online/browser-information/')

    #driver.get('https://2ip.ru')

    time.sleep(14)
    driver.close()

last_proxy = 1


while True:

    if last_proxy > 3:
        last_proxy = 1

    proxy = proxies[str(last_proxy)]

    if last_proxy == 1 or last_proxy == 2:
        lang = 'nl-NL,nl;q=0.9,en-US;q=0.8'
        tz = 'Europe/Amsterdam'
    else:
        lang = 'ru-RU,ru;q=0.9,en-US;q=0.8'
        tz = 'Europe/Moscow'

    print(f'{datetime.now()}, Proxy: {proxy}, ID: {last_proxy}, Lang: {lang}, TZ: {tz}')
    run_task(proxy=proxy, language=lang, timezone=tz)

    last_proxy += 1

    time.sleep(30)


