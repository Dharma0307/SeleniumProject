import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)

driver.get("https://www.google.com/")

search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_input.send_keys("Automation Step by step")

search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)
search_button.click()

time.sleep(2)

driver.close()
driver.quit()

print("Test Completed")
