from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Install ChromeDriver
chrome_driver_path = ChromeDriverManager().install()

# Create WebDriver instance
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.google.com/")

time.sleep(2)
driver.close()
driver.quit()

print("Test Completed")
