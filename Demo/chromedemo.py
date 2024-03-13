from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)

driver.get("https://www.google.com/")
print(driver.title)
driver.close()
driver.quit()
print("completed")
