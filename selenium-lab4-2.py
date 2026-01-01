from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
from func import get_phone_number, get_name, get_email, get_random_yaroslavl_address, make_menu

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument(f'--user-agent={custom_user_agent}')

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

driver.get('https://ylilit.ru/cart')

timers = [0.3, 0.4, 0.5]

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

updated_value = driver.execute_script("return window.cart;")
print(f"The updated variable value is: {updated_value}")

time.sleep(5)

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

