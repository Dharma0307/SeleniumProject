from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# implicit wait
driver.implicitly_wait(10)

driver.get("https://www.google.com/")

# Wait for the search input field to be visible
search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_input.send_keys("Python tutorials")

# Wait for the search button to be clickable and then click it
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)
search_button.click()

print("Test Completed")
driver.close()
driver.quit()
