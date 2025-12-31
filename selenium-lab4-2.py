from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ylilit.ru/cart')


#driver.execute_script("window.cart= '{}';")



driver.execute_script("window.cart['1112'] = '[]';")

driver.execute_script('window.cart["1112"] = [1,"https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg","2050","Шашлык из свиной шеи","1000"];')
#driver.execute_script("alert(cart)")
# driver.execute_script(f"window.cart['1112'][1] = 'https://ylilit.ru/wp-content/uploads/2020/12/DSC_6561-scaled.jpg';")
# driver.execute_script(f"window.cart['1112'][2] = '2050';")
# driver.execute_script(f"window.cart['1112'][3] = 'Шашлык из свиной шеи';")
# driver.execute_script(f"window.cart['1112'][4]=1 = '100';")

updated_value = driver.execute_script("return window.cart;")
print(f"The updated variable value is: {updated_value}")



#driver.find_element("id", "rcmloginsubmit").click()

time.sleep(50)

