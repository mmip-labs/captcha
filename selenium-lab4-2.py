from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import random
from func import get_phone_number, get_name, get_email, get_random_yaroslavl_address

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ylilit.ru/cart')

timers = [0.4, 0.5, 0.6, 0.7]

#driver.execute_script("window.cart= '{}';")



driver.execute_script("window.cart['1112'] = '[]';")

driver.execute_script('window.cart["1112"] = [1,"https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg","2050","Шашлык из свиной шеи","1000"];')

# driver.execute_script(f"window.cart['1112'][0] = 1;")
# driver.execute_script(f"window.cart['1112'][1] = 'https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg';")
# driver.execute_script(f"window.cart['1112'][2] = '2050';")
# driver.execute_script(f"window.cart['1112'][3] = 'Шашлык из свиной шеи';")
# driver.execute_script(f"window.cart['1112'][4] = '100';")

updated_value = driver.execute_script("return window.cart;")
print(f"The updated variable value is: {updated_value}")



for digit in get_phone_number():
    driver.find_element(By.ID, "tel").send_keys(f'{digit}')
    timeout = random.choice(timers)
    time.sleep(timeout)

for char in get_name():
    driver.find_element(By.ID, "name").send_keys(f'{char}')
    timeout = random.choice(timers)
    time.sleep(timeout)

for email in get_email():
    driver.find_element(By.ID, "mail").send_keys(f'{email}')
    timeout = random.choice(timers)
    time.sleep(timeout)

for address in get_random_yaroslavl_address():
    driver.find_element(By.ID, "adress").send_keys(f'{address}')
    time.sleep(0.5)


driver.find_element(By.CLASS_NAME, "sendCart").click()

#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(10)

