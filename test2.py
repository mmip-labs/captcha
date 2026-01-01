from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from emunium import EmuniumSelenium

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
emunium = EmuniumSelenium(driver)

driver.get('https://duckduckgo.com/')

# Wait for the search field to be clickable and type your query
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-state="suggesting"]')))
emunium.type_at(element, 'Automating searches')

# Find and click the search button
submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Search"]')))
emunium.click_at(submit)

driver.quit()