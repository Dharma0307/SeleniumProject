from selenium.webdriver.common.by import By
from Demo.POMDemo.Pages.locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_Name = Locators.username_textbox_Name
        self.password_textbox_Name = Locators.password_textbox_Name
        self.login_button_selector = Locators.login_button_selector

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_Name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_Name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_Name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_Name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_selector).click()
