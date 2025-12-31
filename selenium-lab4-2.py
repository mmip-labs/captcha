from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ylilit.ru/cart')


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

driver.find_element(By.ID, "tel").send_keys('+7 (111) 111-11-11')
time.sleep(3)

driver.find_element(By.ID, "name").send_keys('Ilon Mask')
time.sleep(4)

driver.find_element(By.ID, "mail").send_keys('elon_mask@gmail.com')
time.sleep(3)

driver.find_element(By.ID, "adress").send_keys('Los Angeles, CA')
time.sleep(5)

driver.find_element(By.CLASS_NAME, "sendCart").click()

#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(20)

