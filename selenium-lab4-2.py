from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
from func import get_phone_number, get_name, get_email, get_random_yaroslavl_address, make_menu, random_lang
from func import random_timezone
from fake_useragent import UserAgent


ua = UserAgent()
user_agent = ua.random

timezone = random_timezone()

print(user_agent)

chrome_options = webdriver.ChromeOptions()

# Set language
# language = random_lang()
# chrome_options.add_argument(f'--lang={language}')
# chrome_options.add_argument(f'--accept-lang={language}')

widths = [1366, 1440, 1536]
heights = [768, 900, 960]

chrome_options.add_argument(f"--window-size={random.choice(widths)},{random.choice(heights)}")

# Disable Features That Might Expose Automation
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

#chrome_options.add_argument("--headless=new")


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# Set time zone
# driver.execute_cdp_cmd(
#     "Emulation.setTimezoneOverride",
#     {"timezoneId": timezone}
# )

# Unset webdriver=true
driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});
""")

# Maximize windows
driver.maximize_window()

# Get page
driver.get('https://ylilit.ru/cart')

timers = [0.2, 0.3]

dishes = make_menu()

dish_id = random.choice(list(dishes.keys()))
dish_name = dishes[dish_id][0]
dish_value = dishes[dish_id][1]
dish_img = dishes[dish_id][2]
dish_price = dishes[dish_id][3]


driver.execute_script("window.cart['1112'] = '[]';")

driver.execute_script(f'window.cart["1112"] = [1,"{dish_img}","{dish_price}","{dish_name}","{dish_price}"];')


#driver.execute_script('window.cart["1112"] = [1,"https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg","2050","Шашлык из свиной шеи","1000"];')

# driver.execute_script(f"window.cart['1112'][0] = 1;")
# driver.execute_script(f"window.cart['1112'][1] = 'https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg';")
# driver.execute_script(f"window.cart['1112'][2] = '2050';")
# driver.execute_script(f"window.cart['1112'][3] = 'Шашлык из свиной шеи';")
# driver.execute_script(f"window.cart['1112'][4] = '100';")

#updated_value = driver.execute_script("return window.cart;")
#print(f"The updated variable value is: {updated_value}")

time.sleep(random.choice([3,8]))

for digit in get_phone_number():
    driver.find_element(By.ID, "tel").send_keys(f'{digit}')
    timeout = random.choice(timers)
    time.sleep(timeout)

time.sleep(random.choice([2,3,4,5]))

for char in get_name():
    driver.find_element(By.ID, "name").send_keys(f'{char}')
    timeout = random.choice(timers)
    time.sleep(timeout)

time.sleep(random.choice([2,3,4,5]))

for email in get_email():
    driver.find_element(By.ID, "mail").send_keys(f'{email}')
    timeout = random.choice(timers)
    time.sleep(timeout)

time.sleep(random.choice([2,3,4,5]))

for address in get_random_yaroslavl_address():
    driver.find_element(By.ID, "adress").send_keys(f'{address}')
    time.sleep(0.5)

time.sleep(random.choice([2,3,4,5]))

driver.find_element(By.CLASS_NAME, "sendCart").click()

#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(40)

