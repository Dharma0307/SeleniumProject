from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_input.send_keys("python tutorial")


search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)
search_button.click()
