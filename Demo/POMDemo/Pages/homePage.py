from selenium.webdriver.common.by import By
from Demo.POMDemo.Pages.locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_welcome(self):
        self.driver.find_element(By.CLASS_NAME, self.welcome_link_id).click()

    def logout_link(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()
